import unittest
import time

from api_requests.dummy_json_todos_requests import DummyJsonTodosRequests


class TestGetRandomTodo(unittest.TestCase):

    def setUp(self):
        self.request_handler = DummyJsonTodosRequests()

    def test_get_a_random_todo(self):
        start_time = time.time()
        response = self.request_handler.a_random_todo()
        end_time = time.time()
        expected_status_code = 200
        expected_api_status = "OK"
        actual_response = response.reason
        expected_todo = response.json()
        todo = "todo"
        expected_completed = response.json()
        completed = "completed"
        expected_user_id = 51
        expected_time = 5000
        actual_time = (end_time-start_time)*1000
        self.assertEqual(expected_status_code, response.status_code)
        self.assertEqual(expected_api_status, actual_response)
        self.assertIn(todo, expected_todo)
        self.assertIn(completed, expected_completed)
        self.assertGreater(expected_user_id, response.json()["userId"])
        self.assertLess(actual_time, expected_time)







