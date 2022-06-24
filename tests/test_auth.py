# Auth tests

import os
from fastapi import FastAPI
from fastapi.testclient import TestClient

import requests
from app import app
from fastapi.encoders import jsonable_encoder

from faker import Faker

fake = Faker()
client = TestClient(app)
client.base_url = os.environ.get("URL_LOCAL")


class AuthTestHelper:
  
		def get_token():
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
		response = client.post(
				"/api/login",
				json={
					"user": os.environ.get("EMAIL_TEST"),
					"password": "somepass"
				},
		)
		assert response.status_code == 200
		
def test_verify_token():
		response = client.post(
		"/api/verify/token",
		headers={"Authorization": f"Bearer {AuthTestHelper.get_token()}"},
		json={
				"user": os.environ.get("EMAIL_TEST"),
				"password": "somepass"
			},
		)
		assert response.status_code == 200
  
  
    