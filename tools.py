import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


def clean_company_name(company):
    return company.strip().title()


def search_company(company):

    response = client.search(
        query=f"{company} company overview CEO headquarters products competitors",
        search_depth="advanced",
        max_results=5
    )

    text = ""
    sources = []

    for item in response["results"]:
        text += item["content"] + "\n\n"
        sources.append(item["url"])

    return {
        "text": text,
        "sources": sources
    }


def latest_news(company):

    response = client.search(
        query=f"{company} latest news",
        search_depth="advanced",
        max_results=5
    )

    result = ""

    for item in response["results"]:
        result += "- " + item["title"] + "\n"

    return result