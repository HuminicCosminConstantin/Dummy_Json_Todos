import requests

class DummyJsonTodosRequests:

    BASE_URL = "https://dummyjson.com/todos"

    def get_all_todos(self):
        all_todos = self.BASE_URL
        response = requests.get(url=all_todos)
        return response

    def a_single_todo(self):
        a_single_todo = f'{self.BASE_URL}/{id}'
        response = requests.get(url=a_single_todo)
        return response

    def a_random_todo(self):
        a_random_todo = f'{self.BASE_URL}/random'
        response = requests.get(url=a_random_todo)
        return response

    def limit_and_skip_todos(self, limit=None, skip=None):
        limit_and_skip_todos = self.BASE_URL
        query_params = {}
        if limit is not None:
            query_params.update({"limit":limit})
        if skip is not None:
            query_params.update({"skip":skip})
        response = requests.get(url=limit_and_skip_todos, params=query_params)
        return response

    def get_all_todos_by_user_id(self):
        get_all_todos_by_user_id = f'{self.BASE_URL}/user/{id}'
        response = requests.get(url=get_all_todos_by_user_id)
        return response

    def post_add_a_new_todo(self):
        add_a_new_todo = f'{self.BASE_URL}/add'
        response = requests.post(url=add_a_new_todo)
        return response

    def patch_update_a_todo(self):
        update_a_todo = f'{self.BASE_URL}/{id}'
        response = requests.get(url=update_a_todo)
        return response

    def delete_a_todo(self):
        delete_a_todo = f'{self.BASE_URL}/{id}'
        response = requests.get(url=delete_a_todo)
        return response

obj = DummyJsonTodosRequests()
response1 = obj.get_all_todos()
print(response1.status_code)
print(response1.json())











