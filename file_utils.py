import json

from api_utils import fetch_posts


def save_posts_to_file(user_id, filename):
    data = fetch_posts(user_id)

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    return f"Data saved to {filename}"


def read_posts_from_file(filename):
    with open(filename, "r") as file:
        data = json.load(file)

    return data


if __name__ == "__main__":
    save_posts_to_file(1, "posts.json")

    loaded_data = read_posts_from_file("posts.json")

    print(loaded_data)