import unittest

from api_requests.dummy_json_todos_requests import DummyJsonTodosRequests

class TestGetAllTodos(unittest.TestCase):

    """
    Testam ruta Get/todos
    """
    def setUp(self):
        self.requests_handler = DummyJsonTodosRequests()

    """
    Verificam:
     - status ca status code este 200
     - in response, avem cheia status cu valoarea OK
     - 
    """
    def test_get_all_todos(self):
        response = self.requests_handler.get_all_todos()
        expected_status_code = 200
        actual_api_status = response.reason
        expected_number_todos = 30
        expected_api_status = "OK"
        self.assertEqual(expected_status_code, response.status_code)
        # self.assertEqual(expected_number_todos, response.json()["limit"])
        self.assertEqual(expected_api_status, actual_api_status)
        self.assertEqual(expected_number_todos, len(response.json()))





