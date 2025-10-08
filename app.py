from dotenv import load_dotenv
load_dotenv()

from travel_assistant_pkg.team import create_travel_team

def sample_query() -> None:
    team = create_travel_team()
    prompt = (
      "I want to fly from Bangalore to London on Dec 12, return Dec 16, economy, "
      "prefer window seat and vegetarian meal. Find a mid-range hotel City Central with gym and breakfast."
    )

team.print_response(prompt, stream=True)

if __name__ == "__main__":
    sample_query()