# from src.tools.tools import web_search, scrape_url
# from rich import print

from src.pipelines.pipeline import run_research_pipeline

# output = web_search("Latest news on AI technology")

# print(output)


# result = scrape_url("https://indianexpress.com/section/technology/artificial-intelligence/")

# print(result)


# -- invoke the web_search tool with a query 
# web_search_response = web_search.invoke("what os the latest research on using ai for climate change mitigation?")

# print(web_search_response)


topic = "The impact of AI on the job market in 2026"
run_research_pipeline(topic)