# Trello-API-Python-Requests

## Description
This project automates interactions with the Trello API using Python and pytest. The tests cover various functionalities such as creating and deleting boards, creating lists and cards, and verifying the existence of these elements. The project leverages the requests library to make HTTP requests to the Trello API and includes fixtures for managing API credentials and endpoints.

## Features
- Create and manage Trello boards
- Create and manage lists within boards
- Create and manage cards within lists
- Move cards between lists
- Verify board, list, and card properties

## Table of Contents
1. [Description](#description)
2. [Features](#features)
3. [Endpoints File](#endpoints-file)
4. [Ids Directory](#ids-directory)
5. [Test Files](#test-files)
    - [Conftest File](#conftest.file)
    - [End To End Test File](#end-to-end-test-file)
6. [Example Template](#example-template)
7. [Testing Markers Configuration](#testing-markers-configuration)
8. [Running the Tests](#running-the-tests)
   - [Prerequisites](#prerequisites) 
   - [Execute the Tests](#execute-the-tests)
9. [License](#license) 
10. [Contact Information](#contact-information) 
11. [Happy Testing](#happy-testing)

## Endpoints File
This file defines the base URL for the Trello API and specific endpoints for boards and cards.

- **File**: []()

### Imports
No imports needed in this file.

### Variables
The file contains constants for the base URL and endpoints.

```python
BASE_URL = "https://api.trello.com"
BOARD_ENDPOINT = f"{BASE_URL}/1/boards/"
CARD_ENDPOINT = f"{BASE_URL}/1/cards"
```

*Explanation*:

- **BASE_URL**: The base URL for the Trello API.

- **BOARD_ENDPOINT**: The endpoint URL for creating and managing boards.

- **CARD_ENDPOINT**: The endpoint URL for creating and managing cards.

### Summary
The `endpoints.py` file provides the essential URLs needed for interacting with the Trello API. It sets the foundation for building and making requests to specific API endpoints for boards and cards.

## Ids Directory
Contains various .txt files with different ids, that's been stored and then passed through the conftest file.

- **Directory**: []()

## Conftest File
This file is responsible for setting up fixtures for the Trello API-based testing. It includes fixtures for API credentials, endpoints, and various IDs needed for the tests.

- **File**: []()

### Imports

```python
import pytest
import requests
from dotenv import load_dotenv
import os
from config.endpoints import BASE_URL, BOARD_ENDPOINT, CARD_ENDPOINT
```

*Explanation*:

- **pytest**: A testing framework for Python that helps in writing and running tests.

- **requests**: A library for making HTTP requests in Python.

- **dotenv.load_dotenv**: A function to load environment variables from a .env file.

- **os**: A module for interacting with the operating system.

- **config.endpoints**: Imports the endpoint URLs defined in the endpoints.py file.

### Fixtures
The file defines several fixtures to manage API credentials, endpoints, and IDs. Starting with the credentials.

```python
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
```

*Explanation*:

- **token**: Fixture to get the Trello API access token from environment variables.

- **api_key**: Fixture to get the Trello API key from environment variables.

- **login_credentials**: Fixture to combine the API key and token into a single dictionary.

### Endpoints Fixtures

```python
@pytest.fixture()
def base_url():
    return BASE_URL

@pytest.fixture()
def board_endpoint():
    return BOARD_ENDPOINT

@pytest.fixture()
def card_endpoint():
    return CARD_ENDPOINT
```

*Explanation*:

- **base_url**: Fixture that returns the base URL for the Trello API.

- **board_endpoint**: Fixture that returns the endpoint URL for managing boards.

- **card_endpoint**: Fixture that returns the endpoint URL for managing cards.

### ID Fixtures

```python
@pytest.fixture()
def to_do_list_id():
    # ... code to read the to_do_list_id ...
    return to_do_list_id

@pytest.fixture()
def to_do_list_card_id():
    # ... code to read the to_do_list_card_id ...
    return to_do_list_card_id

@pytest.fixture()
def done_list_id():
    # ... code to read the done_list_id ...
    return done_list_id
```

*Explanation*:

- **to_do_list_id**: Fixture to read the ID of the "To Do" list from a file.

- **to_do_list_card_id**: Fixture to read the ID of a card in the "To Do" list from a file.

- **done_list_id**: Fixture to read the ID of the "Done" list from a file.

### Fixtures for Other Functionalities

```python
@pytest.fixture()
def return_existing_boards(base_url, login_credentials):
    # ... code to get existing boards ...
    return first_board
```

*Explanation*:

- **return_existing_boards**: Fixture to get the ID of the first existing board.

### Summary
The `conftest.py` file is crucial for setting up and managing fixtures needed for Trello API tests. These fixtures provide API credentials, endpoints, and IDs, ensuring consistent and reusable test setups.





