"""User tests"""

import os

# Serializer
from serializers.user import userObject, usersEntity

# Database
from config.db import conn

from faker import Faker
from app import app
from fastapi.testclient import TestClient
from fastapi.encoders import jsonable_encoder
from test_auth import AuthTestHelper

fake = Faker()
client = TestClient(app)
client.base_url = os.environ.get("URL_LOCAL")


class UserTestHelper:
        """
        User Helper tests
        """

        def get_user_by_email(email: str):
            """
			Get user by email test helper
			"""

            user = userObject(conn.local.user.find_one({"user": email}))
            return jsonable_encoder(user)

def test_list_users():
        """
        Test list users
        """

        token = AuthTestHelper.authenticate_user(os.environ.get("EMAIL_TEST"))
        response = client.get(
                    "/api/users",
                    headers={"Authorization": f"Bearer {token}"})
        assert response.status_code == 200

def test_retrieve_user():
        """
        Test retrieve user
        """

        user = UserTestHelper.get_user_by_email(os.environ.get("EMAIL_TEST"))
        response = client.get(
                    f"/api/users/{user['id']}",
                    headers={"Authorization": f"Bearer {AuthTestHelper.get_token()}"})
        assert response.status_code == 200

def test_create_user():
        """
        Test create user
        """

        response = client.post(
        "/api/users",
        headers={"Authorization": f"Bearer {AuthTestHelper.get_token()}"},
        json={
            "user": fake.first_name()+"@"+fake.domain_name(),
            "password": "somepass",
            "name": fake.name(),
            "surname": fake.text(max_nb_chars=5),
            "second_surname": fake.text(max_nb_chars=5),
            "college": fake.company()
            },
        )
        assert response.status_code == 200

def test_update_user():
        """
        Test update user
        """

        user = UserTestHelper.get_user_by_email(os.environ.get("EMAIL_TEST"))
        response = client.put(
                    f"/api/users/{user['id']}",
                    headers={"Authorization": f"Bearer {AuthTestHelper.get_token()}"},
                    json={
                        "user": os.environ.get("EMAIL_TEST"),
                        "password": "somepass",
                        "name": fake.name(),
                        "surname": fake.text(max_nb_chars=5),
                        "second_surname": fake.text(max_nb_chars=5),
                        "college": fake.company()
                        },
                    )
        assert response.status_code == 200

def test_delete_user():
        """
        Test delete user
        """

        user = UserTestHelper.get_user_by_email(os.environ.get("EMAIL_TEST"))
        response = client.delete(
        f"/api/users/{user['id']}",
        headers={"Authorization": f"Bearer {AuthTestHelper.get_token()}"})
        assert response.status_code == 204
