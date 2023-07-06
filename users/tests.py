import pytest
from model_bakery import baker
from django.urls import reverse


# Create your tests here.
@pytest.fixture
def new_user():
    return baker.make("users.VerificationCode")


class TestUser:
    @pytest.mark.django_db
    def test_send_code(self, client):
        url = reverse("send-code")
        data = {
            "phone": "+998912222222"
        }

        response = client.post(url, data=data)

        assert response.status_code == 200

    @pytest.mark.django_db
    def test_check_code(self, client, new_user):
        url = reverse("check-code")
        data = {
            "phone": new_user.phone,
            "code": "1234",
            "name": "test"
        }
        response = client.post(url, data=data)
        assert response.status_code == 400
