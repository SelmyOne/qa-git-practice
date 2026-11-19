def test_completed_todo():
    todo = {"id": 4, "completed": True}
    assert todo["id"] == 4
    # У завершённого дела completed должен быть True.
    assert todo["completed"] is True