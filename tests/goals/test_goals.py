import datetime

import pytest
from django.urls import reverse
from rest_framework import status

from goals.serializers import GoalSerializer

test_date = str(datetime.datetime.now().date())


@pytest.mark.django_db
def test_goal_create(auth_client, goal_category, board_participant):
    url = reverse('goal_create')

    payload = {
            'title': 'Новая цель',
            'category': goal_category.pk,
            'due_date': test_date,
            'description': 'Описание новой цели',
            'status': 1,
            'priority': 1
        }
    response = auth_client.post(
        path=url,
        data=payload
    )
    response_data = response.json()

    assert response.status_code == status.HTTP_201_CREATED
    assert response_data['title'] == payload['title']
    assert response_data['category'] == payload['category']
    assert response_data['due_date'] == payload['due_date']
    assert response_data['description'] == payload['description']
    assert response_data['status'] == payload['status']
    assert response_data['priority'] == payload['priority']


@pytest.mark.django_db
def test_goal_detail(auth_client, goal, test_user, board_participant):
    url = reverse('goal_detail_update_delete', kwargs={'pk': goal.id})
    response = auth_client.get(path=url)
    response_data = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert response_data['user']['id'] == test_user.pk
    assert response_data['user']['username'] == test_user.username
    assert response_data['user']['email'] == test_user.email

    assert response_data['title'] == goal.title
    assert response_data['category'] == goal.category_id
    assert response_data['due_date'] == goal.due_date
    assert response_data['description'] == goal.description
    assert response_data['status'] == goal.status
    assert response_data['priority'] == goal.priority


@pytest.mark.django_db
def test_goal_update(auth_client, goal, test_user, goal_category, board_participant):
    url = reverse('goal_detail_update_delete', kwargs={'pk': goal.id})
    payload = {
            'title': 'Новая цель',
            'category': goal_category.pk,
            'due_date': test_date,
            'description': 'Описание новой цели',
            'status': 1,
            'priority': 1
        }
    response = auth_client.patch(path=url, data=payload)
    response_data = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert response_data['user']['id'] == test_user.pk
    assert response_data['user']['username'] == test_user.username
    assert response_data['user']['email'] == test_user.email

    assert response_data['title'] == payload['title']
    assert response_data['category'] == payload['category']
    assert response_data['due_date'] == payload['due_date']
    assert response_data['description'] == payload['description']
    assert response_data['status'] == payload['status']
    assert response_data['priority'] == payload['priority']


@pytest.mark.django_db
def test_goal_delete(auth_client, goal, board_participant):
    url = reverse('goal_detail_update_delete', kwargs={'pk': goal.id})
    response = auth_client.delete(path=url)

    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_goal_list(auth_client, goal_list, board_participant):
    url = reverse('goal_list')

    response = auth_client.get(path=url)
    expected_response = GoalSerializer(goal_list, many=True).data

    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_response


@pytest.mark.django_db
def test_goal_list_limit(auth_client, goal_list, board_participant):
    url = reverse('goal_list') + '?limit=10'

    response = auth_client.get(path=url)
    expected_response = GoalSerializer(goal_list, many=True).data

    assert response.status_code == status.HTTP_200_OK
    assert response.data['count'] == 10
    assert response.data['next'] is None
    assert response.data['previous'] is None
    assert response.data['results'] == expected_response
