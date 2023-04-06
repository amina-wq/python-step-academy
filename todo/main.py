# Реализуйте класс «Todo». Необходимо хранить в полях класса, 
# поля из объектов: https://jsonplaceholder.typicode.com/todos
# После получения данных с сайта, нужно реализовать метод 
# для сохранения объекта в json и циклом вызвать на каждом объекте Todo метод сохранения.

import requests
import json
from tqdm import tqdm 

class Todo:
    
    def __init__(self, userId: int, id: int, title: str, completed: bool) -> None:
        self.userId = userId
        self.id = id
        self.title = title
        self.completed = completed

    def save_data(self) -> None:
        with open(f'todo/data/{self.id}.json', 'w') as file:
            json.dump({
                "userId": self.userId,
                "id": self.id,
                "title": self.title,
                "completed": self.completed
            }, file)


if __name__ == "__main__":
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    response = response.json()
    todos = []

    for i in tqdm(range(len(response))):
        resp = requests.get(f'https://jsonplaceholder.typicode.com/todos/{i+1}')
        resp = resp.json()
        todos.append(Todo(**resp))

    for todo in todos:
        todo.save_data()