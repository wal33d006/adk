import logging
import requests
from google.adk.agents import Agent

logger = logging.getLogger(__name__)

def find_job(job_skill: str):
    """Given a job skill find out the latest relevant jobs.

    Args:
        job_skill: The skill to find the jobs for

    Returns:
        The list of relevant jobs
    """

    url = f"https://jobicy.com/api/v2/remote-jobs?tag={job_skill}&count=10"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        logger.debug(f"Response: {data}")
        return data['jobs']
    except requests.exceptions.HTTPError as err:
        logger.error(f"HTTP error occurred: {err}")
        return None
    except Exception as err:
        logger.error(f"Other error occurred: {err}")
        return None


instruction_prompt = """
    You're a job hunting agent that can find the top jobs for the skill given by the user.
    Make sure you use the find_job tool to answer the question.
    The tool returns data in the JSON format, try to find the "jobs" array for relevant
    information that matches with the user input.
    Find anything that is related to the words mentioned by the user in the data that is
    received from the find_job tool and formulate a response.
"""

root_agent = Agent(
    name="job_agent",
    model="gemini-2.0-flash",
    description="Agent to find top jobs with respect to the category provided by the user",
    instruction=instruction_prompt,
    tools=[find_job]
)
