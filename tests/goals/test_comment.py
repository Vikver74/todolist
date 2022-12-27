import pytest
from django.urls import reverse
from rest_framework import status

from goals.serializers import GoalCommentSerializer


@pytest.mark.django_db
def test_comment_create(auth_client, goal, board_participant):
    url = reverse('goal_comment_create')
    payload = {
        'text': 'Текст комментария',
        'goal': goal.pk
    }
    response = auth_client.post(url, data=payload)
    response_data = response.json()

    assert response.status_code == status.HTTP_201_CREATED
    assert response_data['text'] == payload['text']
    assert response_data['goal'] == payload['goal']


@pytest.mark.django_db
def test_comment_detail(auth_client, test_user, goal_comment, board_participant):
    url = reverse('goal_comment_detail_update_delete', kwargs={'pk': goal_comment.id})
    response = auth_client.get(url)
    response_data = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert response_data['id'] == goal_comment.id
    assert response_data['user']['id'] == test_user.pk
    assert response_data['user']['username'] == test_user.username
    assert response_data['user']['email'] == test_user.email
    assert response_data['text'] == goal_comment.text
    assert response_data['goal'] == goal_comment.goal_id


@pytest.mark.django_db
def test_comment_update(auth_client, test_user, goal_comment, board_participant):
    url = reverse('goal_comment_detail_update_delete', kwargs={'pk': goal_comment.id})
    payload = {
        'text': 'Текст комментария'
    }
    response = auth_client.patch(url, data=payload)
    response_data = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert response_data['id'] == goal_comment.id
    assert response_data['user']['id'] == test_user.pk
    assert response_data['user']['username'] == test_user.username
    assert response_data['user']['email'] == test_user.email
    assert response_data['text'] == payload['text']
    assert response_data['goal'] == goal_comment.goal_id


@pytest.mark.django_db
def test_comment_delete(auth_client, goal_comment, board_participant):
    url = reverse('goal_comment_detail_update_delete', kwargs={'pk': goal_comment.id})
    response = auth_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_comment_list(auth_client, goal_comment_list, board_participant):
    url = reverse('goal_comment_list')
    response = auth_client.get(url)
    expected_response = GoalCommentSerializer(goal_comment_list, many=True).data

    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_response
