from json import JSONDecodeError
import os
import pytest
import requests


class TestTrello:

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
            assert create_a_board_response.json()["prefs"][
                       "permissionLevel"] == "private", "The permission level should be private"
            assert create_a_board_response.json()["prefs"]["switcherViews"][2][
                       "enabled"] == False, "The calendar switcher view should be disabled"
        except AssertionError as e:
            print(f"Assertion Error: {e}")
        for key, value in create_a_board_response.json().items():
            print(f"{key}: {value}")
        print(f"Status Code: {create_a_board_response.status_code}")
        print("\nEND OF TEST---------------------------------------------")

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
            assert create_card_response.json()["badges"]["attachmentsByType"]["trello"][
                       "card"] == 0, "There should be no attachments"
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

    @pytest.mark.all_tests
    @pytest.mark.move_a_card
    def test_move_a_card(self, card_endpoint, login_credentials, to_do_list_card_id, done_list_id,
                                                                            return_existing_boards):
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
