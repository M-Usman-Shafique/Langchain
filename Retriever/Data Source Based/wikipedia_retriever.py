from langchain_community.retrievers import WikipediaRetriever

# Initialize the retriever
# Optional: set language and top_k (most relevant results)
retriever = WikipediaRetriever(top_k_results=2, lang="en")


# Define query
query = "the geopolitical history of india and pakistan from the perspective of a chinese"

# Get relevant Wikipedia documents
docs = retriever.invoke(query)

docs

# Print retrieved content
for i, doc in enumerate(docs):
    print(f"\n--- Result {i+1} ---")
    print(f"Content:\n{doc.page_content}...")  # truncate for display
