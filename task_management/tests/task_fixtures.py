import pytest
from django.utils import timezone


@pytest.fixture
def create_task(authenticated_client, get_user):
    def _create_task(title = "test task", description = "what", status = 'new', deadline = 1):
        response = authenticated_client.post('/api/v1/task/create/', {
            "title": title,
            "description": description,
            "status": status,
            "deadline": timezone.now() + timezone.timedelta(days=deadline)
        })
        return response
    return _create_task



@pytest.fixture
def get_tasks(authenticated_client, create_task):
    create_task(title="Task 1", status="new")
    create_task(title="Task 2", status="in_progress")
    create_task(title="Task 3", status="completed")

    def _get_tasks():
        return authenticated_client.get("/api/v1/task/list/")

    return _get_tasks