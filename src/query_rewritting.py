
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

class QueryReWriting:
	def __init__(self,model:str = "llama-3.3-70b-versatile"):
		self.llm = ChatGroq(api_key = api_key, model_name = model, temperature=0.2)
		self.prompt = """
		You are an expert query rewriting assistant for a Retrieval-Augmented Generation (RAG) system.

		Rewrite the user's query to improve document retrieval while preserving its original intent.

		Rules:
		- Correct spelling and grammatical mistakes.
		- Keep the meaning unchanged.
		- Make the query concise and self-contained.
		- Expand abbreviations only if they are unambiguous.
		- Do not answer the question.
		- Return only the rewritten query.
		"""

	def reWriteQuery(self,query:str)->str:
		llm = self.llm
		input_query = f"{self.prompt} : {query}"
		output_query = llm.invoke(input_query)
		return output_query.content.strip()
		



