import requests


if __name__ == "__main__":
    api_url = "https://cataas.com/cat"
    response = requests.get(api_url)
    with open("random_cat_image.jpg", "wb") as f:
        f.write(response.content)

    print("Random cat image saved as 'random_cat_image.jpg")
