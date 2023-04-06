# Реализуйте в файл utils функционал для получения данных с сайта jsonplaceholder
import requests
from pprint import pprint
from http import HTTPStatus

class JSONPlaceholderUtility:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    @staticmethod
    def get_posts() -> list:
        """
        Get all posts from jsonplaceholder
        Returns:
            list of all posts
        """
        response = requests.get(f'{JSONPlaceholderUtility.BASE_URL}/posts')

        if response.status_code == HTTPStatus.OK:
            return response.json()
        else:
            return None
    
    @staticmethod
    def get_post(post_id: int) -> dict:
        """
        Get post from jsonplaceholder by id
        Args:
            post_id: int
        Returns:
            dictionary with information about post
        """
        response = requests.get(f'{JSONPlaceholderUtility.BASE_URL}/posts/{post_id}')

        if response.status_code == HTTPStatus.OK:
            return response.json()
        else:
            return None

    @staticmethod
    def get_comments(post_id: int) -> list:
        """
        Get comments about post by id
        Args:
            post_id: int
        Returns:
            list of all comments about post
        """
        response = requests.get(f'{JSONPlaceholderUtility.BASE_URL}/posts/{post_id}/comments')

        if response.status_code == HTTPStatus.OK:
            return response.json()
        else:
            return None

    @staticmethod
    def get_users() -> list:
        """
        Get all users from jsonplaceholder
        Returns:
            list of all users
        """
        response = requests.get(f'{JSONPlaceholderUtility.BASE_URL}/users')
        
        if response.status_code == HTTPStatus.OK:
            return response.json()
        else:
            return None


    @staticmethod
    def get_user(user_id) -> dict:
        """
        Get user from jsonplaceholder by id
        Args:
            user_id: int
        Returns:
            dictionary with information about user
        """
        response = requests.get(f'{JSONPlaceholderUtility.BASE_URL}/users/{user_id}')
        
        if response.status_code == HTTPStatus.OK:
            return response.json()
        else:
            return None


if __name__ == "__main__":
    pprint(JSONPlaceholderUtility.get_posts())
    pprint(JSONPlaceholderUtility.get_post(1))
    pprint(JSONPlaceholderUtility.get_comments(1))
    pprint(JSONPlaceholderUtility.get_users())
    pprint(JSONPlaceholderUtility.get_user(1))