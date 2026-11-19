def test_completed_todo():
    todo = {"id": 4, "completed": True}
    assert todo["id"] == 4
    assert todo["completed"] is True