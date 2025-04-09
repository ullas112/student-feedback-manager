# tests/test_feedback_entry.py

import pytest
from edutrack.feedback_entry import collect_feedback

def test_collect_feedback(monkeypatch):
    # Simulate user input: 2 feedback entries, then 'n' to stop
    inputs = iter(["Alice", "8", "y", "Bob", "6", "n"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    feedback_list = collect_feedback()
    assert isinstance(feedback_list, list)
    assert len(feedback_list) == 2
    assert feedback_list[0]['name'] == 'Alice'
    assert feedback_list[1]['score'] == 6
