from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate

# ================ INDEXING ================ #
# Load the transcript of a YouTube video using its ID, not full video URL
video_id = "Gfr50f6ZBvo"
try:
    # If you don’t care which language, this returns the “best” one
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])

    # Flatten it to plain text
    transcript = " ".join(chunk["text"] for chunk in transcript_list)
    print(transcript)

except TranscriptsDisabled:
    print("No captions available for this video.")

# Split the transcript into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.create_documents([transcript])
len(chunks)
chunks[100]

# Create embeddings for the chunks
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
# Store the chunks in a vector store
vector_store = FAISS.from_documents(chunks, embeddings)
# Print the vector store
vector_store.index_to_docstore_id
# Get a particular vector by its ID
vector_store.get_by_ids(['2436bdb8-3f5f-49c6-8915-0c654c888700'])


# ================ RETRIEVAL ================ #
retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})
retriever
retriever.invoke('What is deepmind')

# ================ AUGMENTATION ================ #
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
prompt = PromptTemplate(
    template="""
      You are a helpful assistant.
      Answer ONLY from the provided transcript context.
      If the context is insufficient, just say you don't know.

      {context}
      Question: {question}
    """,
    input_variables = ['context', 'question']
)

question = "is the topic of nuclear fusion discussed in this video? if yes then what was discussed"
# Retrieve relevant documents based on the question
retrieved_docs = retriever.invoke(question)
retrieved_docs

# Combine the content of the retrieved documents into a single context string
context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
context_text

# Prepare the final prompt by combining the context and the question
final_prompt = prompt.invoke({"context": context_text, "question": question})
final_prompt

# ================ GENERATION ================ #
answer = llm.invoke(final_prompt)
print(answer.content)

