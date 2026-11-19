def test_completed_todo():
    todo = {"id": 4, "completed": True}
    assert todo["id"] == 4
    # Проверяем, что дело завершено.
    assert todo["completed"] is True


def test_open_todo():
    todo = {"id": 1, "completed": False}
    assert todo["id"] == 1
    assert todo["completed"] is False