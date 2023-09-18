import time
import unittest

from api_requests.dummy_json_todos_requests import DummyJsonTodosRequests

class TestGetLimitAndSkipTodos(unittest.TestCase):

    def setUp(self):
        self.request_handler = DummyJsonTodosRequests()

    def test_get_limit_and_skip_todos(self):
        start_time = time.time()
        response = self.request_handler.limit_and_skip_todos(limit=3, skip=10)
        end_time = time.time()
        expected_status_code = 200
        expected_api_status = "OK"
        actual_response = response.reason
        expected_limit = 3
        expected_time = 5000
        actual_time = (end_time-start_time)*1000
        expected_todo_key = "todo"
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_api_status, actual_response)
        self.assertEqual(expected_limit, response.json()["limit"])
        self.assertLess(actual_time, expected_time)
        for i in range(len(response.json()["todos"])):
            actual_todo_key = response.json()["todos"][i]
            self.assertIn(expected_todo_key, actual_todo_key)
        for i in range(len(response.json()["todos"])):
            id_value = response.json()["todos"][i]["id"]
            self.assertTrue(isinstance(id_value, int))








        # expected_id_1 = response.json()["todos"][0][id]
        # print(expected_id_1)



