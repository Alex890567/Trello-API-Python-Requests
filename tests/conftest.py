import pytest
import requests
from dotenv import load_dotenv
import os
from config.endpoints import BASE_URL, BOARD_ENDPOINT, CARD_ENDPOINT

env_path = os.path.join(os.path.dirname(__file__), '..', 'configuration.env')
load_dotenv(env_path)

# CREDENTIALS

@pytest.fixture()
def token():
    token = os.getenv("ACCESS_TOKEN")
    return token

@pytest.fixture()
def api_key():
    api_key = os.getenv("API_KEY")
    return api_key


@pytest.fixture()
def login_credentials(api_key, token):
    return {
        "key": api_key,
        "token": token
    }

# ENDPOINTS

@pytest.fixture()
def base_url():
    return BASE_URL

@pytest.fixture()
def board_endpoint():
    return BOARD_ENDPOINT

@pytest.fixture()
def card_endpoint():
    return CARD_ENDPOINT

# ID'S

@pytest.fixture()
def to_do_list_id():
    script_dir = os.path.dirname(__file__)
    ids_dir = os.path.join(script_dir, "ids")
    os.makedirs(ids_dir, exist_ok=True)
    file_path = os.path.join(ids_dir, "to_do_list_id.txt")
    with open(file_path, "r") as f:
        return f.read()

@pytest.fixture()
def to_do_list_card_id():
    script_dir = os.path.dirname(__file__)
    ids_dir = os.path.join(script_dir, "ids")
    os.makedirs(ids_dir, exist_ok=True)
    file_path = os.path.join(ids_dir, "to_do_list_card_id.txt")
    with open(file_path, "r") as f:
        return f.read()

@pytest.fixture()
def done_list_id():
    script_dir = os.path.dirname(__file__)
    ids_dir = os.path.join(script_dir, "ids")
    os.makedirs(ids_dir, exist_ok=True)
    file_path = os.path.join(ids_dir, "done_list_id.txt")
    with open(file_path, "r") as f:
        return f.read()

# OTHER FUNCTIONALITIES

@pytest.fixture()
def return_existing_boards(base_url, login_credentials):
    response = requests.get(f"{base_url}/1/members/me/boards", params=login_credentials)
    first_board = None
    try:
        if len(response.json()) == 0:
            print("No boards")
        else:
            first_board = response.json()[0]["id"]
    except IndexError as e:
        print(f"Index Error: {e}")
    return first_board

