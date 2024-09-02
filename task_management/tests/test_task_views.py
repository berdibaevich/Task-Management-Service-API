from rest_framework import status

def test_create_task_authenticated(create_task):
    response = create_task()
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['title'] == 'test task'


def test_create_task_no_auth(client):
    response = client.post('/api/v1/task/create/', {
        'title': 'Unauthorized Task',
        'description': 'Unauthorized Description',
        'status': 'new'
    })
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_get_task_list(get_tasks):
    response = get_tasks()

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 3
    assert any(task['title'] == "Task 1" for task in response.data)
    assert any(task['title'] == "Task 2" for task in response.data)
    assert any(task['title'] == "Task 3" for task in response.data)



def test_task_by_status(authenticated_client, create_task):
    create_task(title = "task 1", status = "new")
    create_task(title = "task 2", status = "new")
    create_task(title = "task 3", status = "in_progress")

    response = authenticated_client.get("/api/v1/task/list/", {'status': 'new'})

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2
    assert response.data[0]['title'] == 'task 1'
    assert response.data[1]['title'] == 'task 2'



def test_task_detail(authenticated_client, create_task):
    response = create_task(title="task 2", description="what", status="new", deadline=1)
    task_id = response.data['id']

    response = authenticated_client.get(f"/api/v1/task/detail/{task_id}/")

    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == "task 2"
    assert response.data['description'] == "what"
    assert response.data['status'] == "new"


def test_task_detail_not_found(authenticated_client):
    response = authenticated_client.get("/api/v1/task/detail/2321/")

    assert response.status_code == status.HTTP_404_NOT_FOUND