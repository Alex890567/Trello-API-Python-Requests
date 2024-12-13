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
6. [Example Template Configuration](#example-template-configuration)
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

## Test Files

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

## End To End Test File
This file contains end-to-end tests for various Trello API functionalities using pytest.

- **File**: []()

### Imports

```python
from json import JSONDecodeError
import os
import pytest
import requests
```

*Explanation*:

- **json.JSONDecodeError**: Exception for JSON decoding errors.

- **os**: A module for interacting with the operating system.

- **pytest**: A testing framework for Python.

- **requests**: A library for making HTTP requests in Python.

### Test Class and Functions
The file defines a test class `TestTrello` containing multiple test functions.

```python
class TestTrello:
```

#### test_create_a_board Function
This test function is responsible for creating a new board on Trello and verifying its attributes. It checks if the board is created with the correct name, status, and permissions.

```python
@pytest.mark.all_tests
@pytest.mark.create_board
def test_create_a_board(self, board_endpoint, login_credentials):
    board_name = {"name": "Python_Requests_Board"}
    params = {**login_credentials, **board_name}

    create_a_board_response = requests.post(board_endpoint, params=params)

    try:
        assert create_a_board_response.status_code == 200, "Status code should be 200"
        assert create_a_board_response.json()["name"] == "Python_Requests_Board", "The name is not as expected"
        assert create_a_board_response.json()["closed"] is False, "The board should be open"
        assert create_a_board_response.json()["prefs"]["permissionLevel"] == "private", "The permission level should be private"
        assert create_a_board_response.json()["prefs"]["switcherViews"][2]["enabled"] == False, "The calendar switcher view should be disabled"
    except AssertionError as e:
        print(f"Assertion Error: {e}")
    for key, value in create_a_board_response.json().items():
        print(f"{key}: {value}")
    print(f"Status Code: {create_a_board_response.status_code}")
    print("\nEND OF TEST---------------------------------------------")
```

*Explanation*:

- **test_create_a_board**: Marks the test for creating a board.

- **board_name**: Defines the name of the new board.

- **params**: Combines login credentials with the board name.

- **create_a_board_response**: Sends a POST request to create the board.

- **Assertions**: Checks if the board creation was successful and verifies the attributes like name, status, and permissions.

- **Error Handling**: Prints any assertion errors.

- **Output**: Prints the response details and status code.

#### test_get_all_boards Function
This test function retrieves all boards for a user and verifies the response. It checks if the API returns the boards and prints their details.

```python
@pytest.mark.all_tests
@pytest.mark.get_all_boards
def test_get_all_boards(self, base_url, login_credentials):
    get_all_boards_response = requests.get(f"{base_url}/1/members/me/boards", params=login_credentials)
    boards = get_all_boards_response.json()

    try:
        assert get_all_boards_response.status_code == 200, "The status code should be 200"
    except AssertionError as e:
        print(f"\nAssertion Error: {e}")
    try:
        if len(boards) == 0:
            print("\nNo boards available")
        else:
            cnt = 0
            for board in boards:
                cnt += 1
                print(f"\n{cnt} Board ID: {board['id']}, Name: {board['name']}")
    except IndexError as e2:
        print(f"\nIndex Error: {e2}")
    print(f"\nStatus Code: {get_all_boards_response.status_code}")
    print("\nEND OF TEST---------------------------------------------")
```

- **test_get_all_boards**: Marks the test for retrieving all boards.

- **get_all_boards_response**: Sends a GET request to fetch all boards.

- **Assertions**: Checks if the request was successful (status code 200).

- **Board Details**: Prints the details of each board retrieved.

- **Error Handling**: Prints assertion and index errors.

- **Output**: Prints the status code and response details.

#### test_get_single_board Function
This test function retrieves a single board's details using its ID and verifies the response. It checks if the board details are correctly fetched.

```python
@pytest.mark.all_tests
@pytest.mark.get_single_board
def test_get_single_board(self, board_endpoint, login_credentials, return_existing_boards):
    board_id = return_existing_boards
    url = f"{board_endpoint}{board_id}"

    get_single_board_response = requests.get(url, params=login_credentials)

    try:
        for key, value in get_single_board_response.json().items():
            print(f"\n{key}: {value}")
    except ValueError as e:
        print(f"\nValue Error: {e}")
    try:
        assert get_single_board_response.status_code == 200, "The status code should be 200"
    except AssertionError as e2:
        print(f"\nAssertion Error: {e2}")
    print(f"\nStatus Code: {get_single_board_response.status_code}")
    print("\nEND OF TEST---------------------------------------------")
```

*Explanation*:

- **test_get_single_board**: Marks the test for retrieving a single board.

- **board_id**: Gets the ID of the board to retrieve.

- **get_single_board_response**: Sends a GET request to fetch the board details.

- **Board Details**: Prints the details of the board.

- **Assertions**: Checks if the request was successful (status code 200).

- **Error Handling**: Prints value and assertion errors.

- **Output**: Prints the status code and response details.

#### test_create_to_do_list Function
This test function creates a "To Do" list within an existing board and verifies its attributes. It checks if the list is created correctly.

```python
@pytest.mark.all_tests
@pytest.mark.create_to_do_list
def test_create_to_do_list(self, board_endpoint, login_credentials, return_existing_boards):
    board_id = return_existing_boards
    name = {"name": "To Do"}
    params = {**login_credentials, **name}

    script_dir = os.path.dirname(__file__)
    ids_dir = os.path.join(script_dir, "ids")
    os.makedirs(ids_dir, exist_ok=True)
    file_path = os.path.join(ids_dir, "to_do_list_id.txt")

    create_list_response = requests.post(f"{board_endpoint}{board_id}/lists", params=params)
    try:
        assert create_list_response.status_code == 200, "The status code should be 200"
        assert create_list_response.json()["name"] == "To Do", "The name is not as expected"
        assert create_list_response.json()["closed"] is False, "The list should be open"
        assert create_list_response.json()["idBoard"] == board_id, "The Id's do not match"
    except AssertionError as e:
        print(f"\nAssertion Error: {e}")
    try:
        with open(file_path, "w") as f:
            f.write(str(create_list_response.json()["id"]))
        for key, value in create_list_response.json().items():
            print(f"\n{key}: {value}")
    except JSONDecodeError as e2:
        print(f"\nJSON Decode Error: {e2}")
    print(f"\nStatus Code: {create_list_response.status_code}")
    print("\nEND OF TEST---------------------------------------------")
```

*Explanation*:

- **test_create_to_do_list**: Marks the test for creating a "To Do" list.

- **board_id**: Gets the ID of the board to create the list in.

- **name**: Defines the name of the new list.

- **params**: Combines login credentials with the list name.

- **create_list_response**: Sends a POST request to create the list.

- **Assertions**: Checks if the list creation was successful and verifies the attributes like name, status, and board ID.

- **Error Handling**: Prints assertion and JSON decode errors.

- **Output**: Prints the response details and status code.

#### test_create_done_list Function
This test function creates a "Done" list within an existing board and verifies its attributes. It checks if the list is created correctly.

```python
@pytest.mark.all_tests
@pytest.mark.create_done_list
def test_create_done_list(self, board_endpoint, login_credentials, return_existing_boards):
    board_id = return_existing_boards
    name = {"name": "Done"}
    params = {**login_credentials, **name}

    script_dir = os.path.dirname(__file__)
    ids_dir = os.path.join(script_dir, "ids")
    os.makedirs(ids_dir, exist_ok=True)
    file_path = os.path.join(ids_dir, "done_list_id.txt")

    create_list_response = requests.post(f"{board_endpoint}{board_id}/lists", params=params)
    try:
        assert create_list_response.status_code == 200, "The status code should be 200"
        assert create_list_response.json()["name"] == "Done", "The name is not as expected"
        assert create_list_response.json()["closed"] is False, "The list should be open"
        assert create_list_response.json()["idBoard"] == board_id, "The Id's do not match"
    except AssertionError as e:
        print(f"\nAssertion Error: {e}")
    try:
        with open(file_path, "w") as f:
            f.write(str(create_list_response.json()["id"]))
        for key, value in create_list_response.json().items():
            print(f"\n{key}: {value}")
    except JSONDecodeError as e2:
        print(f"\nJSON Decode Error: {e2}")
    print(f"\nStatus Code: {create_list_response.status_code}")
    print("\nEND OF TEST---------------------------------------------")
```

*Explanation*:

- **test_create_done_list**: Marks the test for creating a "Done" list within an existing board.

- **board_id**: Gets the ID of the board to create the list in using the return_existing_boards fixture.

- **name**: Defines the name of the new list as "Done".

- **params**: Combines the login credentials with the list name to form the request parameters.

- **script_dir**: Retrieves the directory of the current script.

- **ids_dir**: Creates a directory to store ID files if it doesn't already exist.

- **file_path**: Defines the path to the file where the ID of the created "Done" list will be stored.

- **create_list_response**: Sends a POST request to the board endpoint with the list creation parameters.

- **Assertions**:

    - **Status Code**: Verifies that the response status code is 200 (OK), indicating successful creation.

    - **Name**: Checks that the name of the created list matches "Done".

    - **Closed**: Ensures that the list is open (not closed).

    - **Board ID**: Confirms that the list is associated with the correct board ID.

- **Error Handling**:

    - Prints any assertion errors encountered during verification.

    - Handles and prints JSON decode errors if the response cannot be parsed.

- **Output**:

    - Writes the ID of the created list to the specified file.

    - Prints the key-value pairs of the response JSON for detailed verification.

    - Prints the status code of the response.

#### test_get_lists_of_a_board Function
This test function retrieves all lists within an existing board and verifies the response. It checks if the lists are fetched correctly.

```python
@pytest.mark.all_tests
@pytest.mark.get_lists_of_a_board
def test_get_lists_of_a_board(self, board_endpoint, login_credentials, return_existing_boards):
    board_id = return_existing_boards

    get_lists_response = requests.get(f"{board_endpoint}{board_id}/lists", params=login_credentials)
    try:
        assert get_lists_response.status_code == 200, "The status code should be 200"
    except AssertionError as e:
        print(f"\nAssertion Error: {e}")
    try:
        for item in get_lists_response.json():
            for key, value in item.items():
                print(f"\n{key}: {value}")
    except JSONDecodeError as e2:
        print(f"\nJSON Decode Error: {e2}")
    print(f"\nStatus code: {get_lists_response.status_code}")
    print("\nEND OF TEST---------------------------------------------")
```

*Explanation*:

- **test_get_lists_of_a_board**: Marks the test for retrieving all lists within a board.

- **board_id**: Gets the ID of the board to fetch the lists from using the return_existing_boards fixture.

- **get_lists_response**: Sends a GET request to the board endpoint with the board ID to fetch the lists.

- **Assertions**:

    - **Status Code**: Verifies that the response status code is 200 (OK), indicating successful retrieval.

- **Error Handling**:

    - Prints any assertion errors encountered during verification.

    - Handles and prints JSON decode errors if the response cannot be parsed.

- **Output**:

    - Iterates through the lists and prints the key-value pairs of each list's JSON response.

    - Prints the status code of the response.

#### test_create_card_on_a_list Function
This test function creates a card within a "To Do" list and verifies its attributes. It checks if the card is created correctly, including attributes such as name, list ID, and board ID.

```python
@pytest.mark.all_tests
@pytest.mark.create_a_card
def test_create_card_on_a_list(self, card_endpoint, login_credentials, to_do_list_id, return_existing_boards):
    id_of_the_list = {"idList": to_do_list_id}
    name_of_the_card = {"name": "Register to Trello"}
    params = {**login_credentials, **id_of_the_list, **name_of_the_card}

    script_dir = os.path.dirname(__file__)
    ids_dir = os.path.join(script_dir, "ids")
    os.makedirs(ids_dir, exist_ok=True)
    file_path = os.path.join(ids_dir, "to_do_list_card_id.txt")

    create_card_response = requests.post(card_endpoint, params=params)

    try:
        assert create_card_response.status_code == 200, "The status code should be 200"
        assert create_card_response.json()["name"] == "Register to Trello", "The name is not as expected"
        assert create_card_response.json()["idList"] == to_do_list_id, "The id's do not match"
        assert create_card_response.json()["idBoard"] == return_existing_boards, "The id's do not match"
        assert create_card_response.json()["badges"]["attachmentsByType"]["trello"]["card"] == 0, "There should be no attachments"
    except AssertionError as e:
        print(f"\nAssertion Error: {e}")
    try:
        with open(file_path, "w") as f:
            f.write(str(create_card_response.json()["id"]))
        for key, value in create_card_response.json().items():
            print(f"\n{key}: {value}")
        print(f"Response: {create_card_response.json()}")
    except JSONDecodeError as e2:
        print(f"\nJSON Decode Error: {e2}")
    print(f"\nStatus code: {create_card_response.status_code}")
    print("\nEND OF TEST---------------------------------------------")
```

*Explanation*:

- **test_create_card_on_a_list**: Marks the test for creating a card within a "To Do" list.

- **id_of_the_list**: Defines the ID of the "To Do" list where the card will be created.

- **name_of_the_card**: Defines the name of the new card as "Register to Trello".

- **params**: Combines the login credentials with the list ID and card name to form the request parameters.

- **script_dir**: Retrieves the directory of the current script.

- **ids_dir**: Creates a directory to store ID files if it doesn't already exist.

- **file_path**: Defines the path to the file where the ID of the created card will be stored.

- **create_card_response**: Sends a POST request to the card endpoint with the card creation parameters.

- **Assertions**:

    - **Status Code**: Verifies that the response status code is 200 (OK), indicating successful creation.
    
    - **Name**: Checks that the name of the created card matches "Register to Trello".
    
    - **List ID**: Ensures that the card is associated with the correct list ID.
    
    - **Board ID**: Confirms that the card is associated with the correct board ID.
    
    - **Attachments**: Verifies that there are no attachments to the card.

- **Error Handling**:

    - Prints any assertion errors encountered during verification.
    
    - Handles and prints JSON decode errors if the response cannot be parsed.

- **Output**:

    - Writes the ID of the created card to the specified file.
    
    - Prints the key-value pairs of the response JSON for detailed verification.
    
    - Prints the status code of the response.

#### test_get_cards_on_a_board Function
This test function retrieves all cards within an existing board and verifies the response. It checks if the cards are fetched correctly, including their details and status.

```python
@pytest.mark.all_tests
@pytest.mark.get_cards_on_a_board
def test_get_cards_on_a_board(self, board_endpoint, login_credentials, return_existing_boards):
    board_id = return_existing_boards

    get_cards_response = requests.get(f"{board_endpoint}{board_id}/cards", params=login_credentials)

    try:
        assert get_cards_response.status_code == 200, "The status code should be 200"
    except AssertionError as e2:
        print(f"\nAssertion Error: {e2}")
    try:
        for item in get_cards_response.json():
            for key, value in item.items():
                print(f"\n{key}: {value}")
    except ValueError as e:
        print(f"\nValue Error: {e}")
    print(f"\nStatus code: {get_cards_response.status_code}")
    print("\nEND OF TEST---------------------------------------------")
```

*Explanation*:

- **test_get_cards_on_a_board**: Marks the test for retrieving all cards within a board.

- **board_id**: Gets the ID of the board to fetch the cards from using the return_existing_boards fixture.

- **get_cards_response**: Sends a GET request to the board endpoint with the board ID to fetch the cards.

- **Assertions**:

    - **Status Code**: Verifies that the response status code is 200 (OK), indicating successful retrieval.

- **Error Handling**:

    - Prints any assertion errors encountered during verification.
    
    - Handles and prints value errors if the response cannot be parsed.

- **Output**:

    - Iterates through the cards and prints the key-value pairs of each card's JSON response.
    
    - Prints the status code of the response.

#### test_move_a_card Function
This test function moves a card from the "To Do" list to the "Done" list and verifies its attributes. It checks if the card is moved correctly, including attributes such as list ID and board ID.

```python
@pytest.mark.all_tests
@pytest.mark.move_a_card
def test_move_a_card(self, card_endpoint, login_credentials, to_do_list_card_id, done_list_id, return_existing_boards):
    card_id = to_do_list_card_id
    id_of_the_new_list = {"idList": done_list_id}
    params = {**login_credentials, **id_of_the_new_list}

    move_card_response = requests.put(f"{card_endpoint}/{card_id}", params=params)

    try:
        assert move_card_response.status_code == 200, "The status code should be 200"
        assert move_card_response.json()["idList"] == done_list_id, "The id's do not match"
        assert move_card_response.json()["idBoard"] == return_existing_boards, "The id's do not match"
        assert move_card_response.json()["name"] == "Register to Trello", "The name is not as expected"
    except AssertionError as e:
        print(f"\nAssertion Error: {e}")
    try:
        for key, value in move_card_response.json().items():
            print(f"\n{key}: {value}")
    except JSONDecodeError as e2:
        print(f"\nJSON Decode Error: {e2}")
    print(f"\nStatus code: {move_card_response.status_code}")
    print("\nEND OF TEST---------------------------------------------")
```

*Explanation*:

- **test_move_a_card**: Marks the test for moving a card from one list to another.

- **card_id**: Gets the ID of the card to be moved.

- **id_of_the_new_list**: Defines the ID of the new list where the card will be moved.

- **params**: Combines the login credentials with the new list ID to form the request parameters.

- **move_card_response**: Sends a PUT request to the card endpoint with the card ID to move the card.

- **Assertions**:

    - **Status Code**: Verifies that the response status code is 200 (OK), indicating successful move.
    
    - **List ID**: Ensures that the card is associated with the correct new list ID.
    
    - **Board ID**: Confirms that the card is still associated with the correct board ID.
    
    - **Name**: Checks that the name of the card remains "Register to Trello".

- **Error Handling**:

    - Prints any assertion errors encountered during verification.
    
    - Handles and prints JSON decode errors if the response cannot be parsed.

- **Output**:

    - Prints the key-value pairs of the response JSON for detailed verification.
    
    - Prints the status code of the response.

#### test_delete_a_board Function
This test function deletes an existing board and verifies the response. It checks if the board is deleted successfully and handles the response accordingly.

```python
@pytest.mark.all_tests
@pytest.mark.delete_a_board
def test_delete_a_board(self, board_endpoint, login_credentials, return_existing_boards):
    board_id = return_existing_boards

    delete_board_response = requests.delete(f"{board_endpoint}{board_id}", params=login_credentials)

    try:
        assert delete_board_response.status_code == 200, "The status code should be 200"
    except AssertionError as e:
        print(f"\nAssertion Error: {e}")
    if delete_board_response.status_code == 200:
        try:
            for key, value in delete_board_response.json().items():
                print(f"\n{key}: {value}")
        except JSONDecodeError as e2:
            print(f"\nJSON Decode Error: {e2}")
    elif delete_board_response.status_code == 400:
        print("\nNo boards remain")
        print(f"\nResponse: {delete_board_response.text}")
    else:
        pass
    print(f"\nStatus code: {delete_board_response.status_code}")
    print("\nEND OF TEST---------------------------------------------")
```

*Explanation*:

- **test_delete_a_board**: Marks the test for deleting a board.

- **board_id**: Gets the ID of the board to be deleted using the return_existing_boards fixture.

- **delete_board_response**: Sends a DELETE request to the board endpoint with the board ID to delete the board.

- **Assertions**:

    - **Status Code**: Verifies that the response status code is 200 (OK), indicating successful deletion.

- **Error Handling**:

    - Prints any assertion errors encountered during verification.
    
    - Handles and prints JSON decode errors if the response cannot be parsed.
    
    - Handles the case where no boards remain (status code 400).

- **Output**:

    - Prints the key-value pairs of the response JSON for detailed verification if the board is deleted successfully.
    
    - Prints the status code of the response.

#### test_get_deleted_board Function
This test function attempts to retrieve a deleted board and verifies the response. It checks if the appropriate error message is returned.

```python
@pytest.mark.all_tests
@pytest.mark.get_deleted_board
def test_get_deleted_board(self, board_endpoint, login_credentials, return_existing_boards):
    board_id = return_existing_boards

    get_deleted_board_response = requests.get(f"{board_endpoint}{board_id}", params=login_credentials)

    try:
        assert get_deleted_board_response.status_code == 400, "The status code should be 400"
    except AssertionError as e:
        print(f"Assertion Error: {e}")

    print(f"\nResponse: {get_deleted_board_response.text}")
    print(f"Status Code: {get_deleted_board_response.status_code}")
    print("\nEND OF TEST---------------------------------------------")
```

*Explanation*:

- **test_get_deleted_board**: Marks the test for attempting to retrieve a deleted board.

- **board_id**: Gets the ID of the deleted board using the return_existing_boards fixture.

- **get_deleted_board_response**: Sends a GET request to the board endpoint with the board ID to fetch the deleted board.

- **Assertions**:

    - **Status Code**: Verifies that the response status code is 400 (Bad Request), indicating that the board has been deleted and cannot be retrieved.

- **Error Handling**:

    - Prints any assertion errors encountered during verification.

- **Output**:

    - Prints the response text for detailed verification.
    
    - Prints the status code of the response.

#### Summary
The `test_end_to_end.py` file contains comprehensive end-to-end tests for various Trello API functionalities. Each test ensures that the operations (creating, retrieving, moving, and deleting boards, lists, and cards) are performed correctly and validated thoroughly.

## Example Template Configuration
The `configuration.env.template` file is an example environment file used to set up environment variables for the project. This file serves as a template, guiding users on how to create their actual environment file (`configuration.env`) without exposing sensitive data in the repository.

- **File**: []()

#### Configuration Environment Setup Instructions

##### 1. Create the Configuration Environment File

- Copy the `configuration.env.template` file and rename it to `configuration.env` by removing the `.template` extension.

##### 2. Edit the Testing Environment File

- Open the newly created `configuration.env` file in a text editor.
- Replace the placeholder values with your actual credentials.

##### 3. Obtain Access Tokens and API Key

- To obtain an API Key, follow the instructions from the official API documentation of Trello: https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/

- To obtain an access Token, follow the instructions from the same official source: https://developer.atlassian.com/cloud/trello/guides/rest-api/authorization/

## Testing Markers Configuration
The .ini file is used to configure and provide descriptions for all the markers utilized in the testing files. These markers help in organizing, categorizing, and selectively running tests based on specific criteria.

- **File**: [Testing Markers Configuration]()

#### Purpose of the .ini File

- **Define Markers**: Specifies and describes each marker used in the testing files.

- **Improve Test Management**: Enhances the organization and readability of tests by providing clear descriptions.

- **Selective Test Execution**: Allows running specific groups of tests based on the markers defined.

## Running The Tests

### Prerequisites
1. **Clone the Repository**: 
     - Clone the repository to your local machine:
       ```bash 
       git clone (link)
       ```
     - Navigate to the Repository Directory:
       ```bash
        cd directory
       ```
2. **Install Dependencies**:
     - In your project directory, install the required dependencies:
       ```bash
       pip install -r requirements.txt
       ```
3. **Python**: 
     - Ensure you have Python installed on your machine. Download it from [python.org](https://www.python.org/).

### Execute the Tests
To ensure the proper functioning of this project, tests have been set up and can be run in various ways:

#### 1. From PyCharm:

     - If you are using PyCharm as your IDE, you can run the tests directly from the IDE's configuration settings:
     
        - Open PyCharm and navigate to the `Run` menu.
        - Run the tests or specific test, from the existing configurations.

#### 2. Through the Terminal:

     - You can also run the tests from the terminal using standard testing commands. Make sure the virtual environment is activated before running the tests.

## License
All rights reserved. See the [LICENSE](./LICENSE) file for more details.

## Contact Information
For any questions or feedback, feel free to reach out to me at alexparlaloglou@gmail.com

## Happy Testing!





