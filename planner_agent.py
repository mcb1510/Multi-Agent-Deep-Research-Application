from pydantic import BaseModel, Field
from agents import Agent, Runner
from dotenv import load_dotenv
from search_agent import search_agent
import asyncio

load_dotenv(override=True)
MODEL_NAME ="gpt-5.4-mini"
HOW_MANY_SEARCHES = 3

INSTRUCTIONS = f"""
You are a research assistant. Given a user query, come up with a set of web searches
to perform to best answer the query. Output {HOW_MANY_SEARCHES} terms to query for.
"""

class WebSearchItem(BaseModel):
    reason: str = Field(description="Your reasoning for why this search is important to the query.")
    query: str = Field(description="The search term to use for the web search.")

class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem] = Field(description="A list of web searches to perform to best answer the query.")

planner_agent = Agent(name="Planner Agent", instructions=INSTRUCTIONS, model=MODEL_NAME, output_type=WebSearchPlan)

async def search(item: WebSearchItem) -> str | None:
    """ Perform a search for the query """
    input_message = f"Search term: {item.query}\nReason for searching: {item.reason}"
    return await Runner.run(search_agent, input_message)

async def plan_searches(query:str) -> WebSearchPlan:
    """ Plan the searches to perform for the query """
    result = await Runner.run(planner_agent, f"Query: {query}")
    return result.final_output

async def perform_searches(search_plan: WebSearchPlan) -> list[str]:
    """ Perform the searches to perform for the query"""
    tasks = [search(item) for item in search_plan.searches]
    return await asyncio.gather(*tasks)