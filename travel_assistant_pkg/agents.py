from agno.agent import Agent
from agno.models.groq import Groq

from .tools import AirlineSearchTool, HotelSearchTool

USER_FLIGHT_PREFERENCES_DOC = (
  """
    You maintain traveler flight preferences:
    - Cheap vs Luxury bias
    - Preferred seats (aisle/window)
    - Meals (e.g., vegetarian)
    - Cabin (Economy/Premium/Business)
    Use these preferences when ranking flight options. Always justify the top pick briefly.
  """
)

USER_HOTEL_PREFERENCES_DOC = (
  """
    You maintain traveler hotel preferences:
    - Amenities importance (wifi, gym, breakfast, pool, spa)
    - Bed count
    - Check-in/out flexibility
    Use these preferences to rank hotels and explain why the choice fits.
  """
)

def create_flight_agent() -> Agent:
    return Agent(
        name="Flight Agent",
        role="Search and recommend flights using airline providers",
        model=Groq(id="llama-3.1-8b-instant"),
        tools=[AirlineSearchTool()],
        instructions=[
            "Call AirlineSearchTool first to get candidate flights.",
            "Use web search only to verify airport codes or baggage policy if asked.",
            USER_FLIGHT_PREFERENCES_DOC,
            "Output a concise flight proposal with price, times, and seat/meal notes.",
        ],
        markdown=True,
    )

def create_hotel_agent() -> Agent:
    return Agent(
        name="Hotel Agent",
        role="Search and recommend hotels using partner providers",
        model=Groq(id="llama-3.1-8b-instant"),
        tools=[HotelSearchTool()],
        instructions=[
            "Call HotelSearchTool to get candidate stays.",
            USER_HOTEL_PREFERENCES_DOC,
            "Summarize top 1-2 options with nightly rate, amenities, and rating.",
        ],
        markdown=True,
    )


