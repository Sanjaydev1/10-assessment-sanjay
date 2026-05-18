import requests


def fetch_posts(user_id):
    url = f"https://jsonplaceholder.typicode.com/posts?userId={user_id}"

    try:
        response = requests.get(url, timeout=5)

        response.raise_for_status()

        posts = response.json()

        return {
            "count": len(posts),
            "first_3_titles": [
                post["title"] for post in posts[:3]
            ]
        }

    except requests.exceptions.RequestException as error:
        return {
            "error": str(error)
        }


if __name__ == "__main__":
    result = fetch_posts(1)

    print(result)