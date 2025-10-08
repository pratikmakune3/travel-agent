from agno.team import Team
from agno.models.groq import Groq

from .agents import create_flight_agent, create_hotel_agent

def create_travel_team() -> Team:
    flight_agent = create_flight_agent()
    hotel_agent = create_hotel_agent()

    return Team(
        members=[flight_agent, hotel_agent],
        model=Groq(id="llama-3.1-8b-instant"),
        instructions=[
            "Ask for missing details (dates, origin/destination, budget) if not provided.",
            "Summarize at the end with a proposed itinerary and next steps to book.",
            "If the user mentions a specific airline or brand, prioritize it when reasonable.",
        ],
        markdown=True,
    )