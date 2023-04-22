
import pytest

from rest_framework import status


@pytest.mark.django_db
def test_ad_create(client, user, category):

    data = {
        "name": "Сибирская котята, 3 месяца",
        "author_id": user.username,
        "price": 2500,
        "category_id": category.name,
        "description": "123"

    }

    expected_data = {
        "id": 1,
        "name": "Сибирская котята, 3 месяца",
        "price": 2500,
        "description": "123",
        "is_published": False,
        "image": None,
        "author_id": user.username,
        "category_id": category.name
    }

    response = client.post(f"/ad/", data=data)

    assert response.data == expected_data
    assert response.status_code == status.HTTP_201_CREATED

