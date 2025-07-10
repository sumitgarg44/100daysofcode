"""Data for quiz game"""

import json
import html
import requests


def generate_questions(total_questions=10, level="medium"):
    """Generate questions from Open Trivia DB"""
    tdb_api = (
        f"https://opentdb.com/api.php?amount={total_questions}&"
        f"difficulty={level}&type=boolean"
    )
    question_data = []
    index = 0

    try:
        response = requests.get(tdb_api, timeout=60)
        response.raise_for_status()
        data_list = json.loads(response.text)["results"]

        while index < len(data_list):
            quiz_answer_dict = {}
            index_data = data_list[index]
            quiz_answer_dict["text"] = html.unescape(index_data["question"])
            quiz_answer_dict["answer"] = index_data["correct_answer"]
            question_data.append(quiz_answer_dict)
            index += 1
        return question_data

    except requests.exceptions.HTTPError as e:
        print(f"Failed to generate questions: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"An error occured while generating questions: {e}")
        return None
