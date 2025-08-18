"""Data for quiz game"""

import requests

tdb_api = "https://opentdb.com/api.php"
parameters = {
    "amount": 10,
    "type": "boolean"
}

def generate_questions():
    """Generate questions from Open Trivia DB"""

    try:
        response = requests.get(tdb_api, params=parameters, timeout=60)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"Failed to generate questions: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"An error occured while generating questions: {e}")
        return None

    return response.json()["results"]
