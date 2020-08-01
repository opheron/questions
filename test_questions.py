import json
import pytest

@pytest.fixture
def invalid_data():
   return """{"name": "jane doe", "salary": 9000, "email": "jane.doe@pynative.com",}"""

@pytest.fixture
def valid_data():
    return """{"name": "jane doe", "salary": 9000, "email": "jane.doe@pynative.com"}"""

@pytest.fixture
def questions_data():
    return open('questions.json', 'r').read()

def validate_json(data):
    try:
        questions_dict = json.loads(data)
    except ValueError as err:
        return False
    return True

def test_valid_json_passes(valid_data):
    assert validate_json(valid_data)

def test_invalid_json_fails(invalid_data):
    assert not validate_json(invalid_data)

def test_question_json_passes(questions_data):
    assert validate_json(questions_data)
