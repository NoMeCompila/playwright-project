from http.client import responses

import pytest
from playwright.sync_api import sync_playwright
from urllib3.exceptions import BodyNotHttplibCompatible

BASE_URL = "https://reqres.in/api/users/"


def test_get_user():
    with sync_playwright() as p:

        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        get_user(page)
        get_users_list(page)
        create_nre_user(page)

        browser.close()


def get_user(page):
    response = page.request.get(BASE_URL+"2")
    print(response)
    assert response.status == 200


def get_users_list(page):
    response = page.request.get(BASE_URL+"?page=2")
    assert response.status == 200


def create_nre_user(page):

    body = {
        "name": "Fer",
        "job": "TAE"
    }

    response = page.request.post(BASE_URL, data=body)

    assert response.status == 201
    response_json = response.json()
    assert "id" in response_json
    assert "createdAt" in response_json