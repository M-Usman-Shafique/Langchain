from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser

# Step 1: Lambda to fetch YouTube video transcript
def fetch_transcript(video_id: str) -> str:
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])
        return " ".join(chunk["text"] for chunk in transcript_list)
    except TranscriptsDisabled:
        raise ValueError("No captions available for this video.")

# Step 2: Lambda to split transcript into chunks
def split_text(text: str):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return splitter.create_documents([text])

# Step 3: Lambda to embed & store the transcript in vector store
def store_in_vectorstore(docs):
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vector_store = FAISS.from_documents(docs, embeddings)
    return vector_store

# Indexing chain
indexing_chain = (
    RunnableLambda(fetch_transcript)
    | RunnableLambda(split_text)
    | RunnableLambda(store_in_vectorstore)
)

# Run indexing
video_id = "Gfr50f6ZBvo"
vectorstore = indexing_chain.invoke(video_id)

# Setup retriever
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 4})

# Setup prompt
prompt = ChatPromptTemplate.from_template(
    """
    You are a helpful assistant.
    Answer ONLY from the provided transcript context.
    If the context is insufficient, just say you don't know.

    {context}
    Question: {question}
    """
)

# Setup LLM and output parser
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
parser = StrOutputParser()

# Format retrieved docs
def format_docs(retrieved_docs):
    return "\n\n".join(doc.page_content for doc in retrieved_docs)

# Retrieval + Augmentation
parallel_chain = RunnableParallel({
    'context': retriever | RunnableLambda(format_docs),
    'question': RunnablePassthrough()
})

# Final chain
main_chain = parallel_chain | prompt | llm | parser

# Chain execution
response = main_chain.invoke("Can you summarize the video?")
print(response)
