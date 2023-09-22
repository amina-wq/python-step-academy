import requests
import json


class JSONPlaceholderAPI:
    BASE_URI = "https://jsonplaceholder.typicode.com"

    @classmethod
    def fetch_todos(cls):
        try:
            response = requests.get(f"{cls.BASE_URI}/todos")
            todos = response.json()

            with open("data.json", "w") as file:
                json.dump(todos, file, indent=4)

            print("Данные успешно записаны в data.json")
        except requests.exceptions.RequestException as e:
            print(f"Произошла ошибка при выполнении запроса: {e}")
        except json.JSONDecodeError as e:
            print(f"Произошла ошибка при декодировании JSON: {e}")


if __name__ == "__main__":
    JSONPlaceholderAPI.fetch_todos()
