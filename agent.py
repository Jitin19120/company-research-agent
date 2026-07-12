from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

from prompts import INVESTMENT_PROMPT
from tools import clean_company_name, search_company, latest_news

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=api_key
)


def generate_report(company):

    company = clean_company_name(company)

    search_result = search_company(company)

    search_data = search_result["text"]

    sources = search_result["sources"]

    news = latest_news(company)

    prompt = INVESTMENT_PROMPT.format(
        company=company,
        search_data=search_data,
        news=news
    )

    response = llm.invoke(prompt)

    report = response.content

    # Create outputs folder if it doesn't exist
    os.makedirs("outputs", exist_ok=True)

    file_name = f"outputs/{company}.txt"

    with open(file_name, "w", encoding="utf-8") as file:
        file.write(report)

    return report, sources