
import pytest

from rest_framework import status

from app.serializer import SerializerAdList
from tests.factories import AdFactory


@pytest.mark.django_db
def test_selection(client, user):
    ad_list = AdFactory.create_batch(4)
    data = {
        "name": "test",
        "items": [1, 2]
    }

    expected_data = {
        "id": 1,
        "owner": user.username,
        "name": "test",
        "items": [1, 2]
    }

    response = client.post(f"/selection/", data=data)

    assert response.data == expected_data
    assert response.status_code == status.HTTP_201_CREATED

