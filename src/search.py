import os
from dotenv import load_dotenv
from src.vectorstore import FaissVectorStore
from langchain_groq import ChatGroq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

class RAGSearch:
	def __init__(self, persist_dir: str= "faiss_store", embedding_model:str = "all-MiniLM-L6-v2",model_name:str = "llama-3.3-70b-versatile"):
		self.vectorstore = FaissVectorStore(persist_dir, embedding_model)
		# Load or build vectorstore
		faiss_path = os.path.join(persist_dir, "faiss.index")
		meta_path = os.path.join(persist_dir, "metadata.pk1")
		if not (os.path.exists(faiss_path) and os.path.exists(meta_path)):
			from src.data_loader import load_all_documents
			docs = load_all_documents("./data")
			self.vectorstore.build_from_documents(docs)
		else:
			self.vectorstore.load()

		groq_api_key = api_key
		self.llm = ChatGroq(api_key = groq_api_key, model_name=model_name,temperature=0.1,max_tokens = 1024)
		print(f"Groq LLM initialized: {model_name}")

	def search_and_summarize(self,query:str, top_k:int = 5) -> str:
		results = self.vectorstore.query(query,top_k = top_k)
		texts = [r["metadata"].get("text","") for r in results if r["metadata"]]
		context = "\n\n".join(texts)
		if not context:
			return "No relevant documents found."
		prompt = f"""summarize the following context for the query: '{query}' \n\n Context: '{context}' and the answer is:"""
		response = self.llm.invoke([prompt])
		return response.content

