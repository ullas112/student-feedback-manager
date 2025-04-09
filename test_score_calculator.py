# tests/test_score_calculator.py

import pytest
from edutrack.score_calculator import compute_average_score

def test_average_with_data():
    feedback = [{'name': 'Alice', 'score': 8}, {'name': 'Bob', 'score': 6}]
    avg = compute_average_score(feedback)
    assert avg == 7.0

def test_average_empty_list():
    feedback = []
    avg = compute_average_score(feedback)
    assert avg == 0
