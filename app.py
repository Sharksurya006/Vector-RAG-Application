from src.data_loader import load_all_documents
from src.vectorstore import FaissVectorStore
from src.search import RAGSearch
from src.query_rewritting import QueryReWriting

if __name__ == '__main__':
	docs = load_all_documents("./data")
	store = FaissVectorStore("faiss_store")
	# store.build_from_documents(docs)
	store.load();
	# print(store.query("What is Deep Learning and explain its advantage?", top_k=3))

	rag_search = RAGSearch()
	query = input("Ask whatever you want? ")
	print("=" * 30)
	print(f"Actual query: {query}")
	print("=" * 30)
	rewrite = QueryReWriting()
	print("=" * 30)
	rewritted_query = rewrite.reWriteQuery(query)
	print(f"Rewritted-query: {rewritted_query}")
	print("=" * 30)
	summary = rag_search.search_and_summarize(rewritted_query,top_k=3)
	print("Summary:",summary)
