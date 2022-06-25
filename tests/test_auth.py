"""Auth tests"""

import os
from fastapi.testclient import TestClient
from fastapi.encoders import jsonable_encoder
from app import app
from faker import Faker

fake = Faker()
client = TestClient(app)
client.base_url = os.environ.get("URL_LOCAL")


class AuthTestHelper:
	"""
	Auth Helper tests
	"""

	def get_token():
		"""
		Get token auth test helper
		"""

		response = client.post(
				"/api/login",
				json={
					"user": "jbravonew12@example.com",
					"password": "somepass"
				},
		)
		token = jsonable_encoder(response.content).replace('"', "")
		return token

	def authenticate_user(user: str):
		"""
		Authenticate user test helper
		"""
		response = client.post(
				"/api/login",
				json={
					"user": user,
					"password": "somepass"
				},
		)
		token = jsonable_encoder(response.content).replace('"', "")
		return token

def test_sing_up():
	"""
	Test sing up
	"""

	response = client.post(
			"/api/sign_up",
			json={
				"user": os.environ.get("EMAIL_TEST"),
				"password": "somepass",
				"name": fake.name(),
				"surname": fake.last_name(),
				"second_surname": fake.last_name(),
				"college": fake.company()
			},
	)
	assert response.status_code == 201

def test_loguin():
	"""
	Test loguin
	"""

	response = client.post(
			"/api/login",
			json={
				"user": os.environ.get("EMAIL_TEST"),
				"password": "somepass"
			},
	)
	assert response.status_code == 200

def test_verify_token():
	"""
	Test verify Token
	"""

	response = client.post(
	"/api/verify/token",
	headers={"Authorization": f"Bearer {AuthTestHelper.get_token()}"},
	json={
			"user": os.environ.get("EMAIL_TEST"),
			"password": "somepass"
		},
	)
	assert response.status_code == 200
