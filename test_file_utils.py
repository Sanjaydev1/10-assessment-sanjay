from file_utils import (
    save_posts_to_file,
    read_posts_from_file
)


def test_save_and_read_posts():
    filename = "test_posts.json"

    save_posts_to_file(1, filename)

    data = read_posts_from_file(filename)

    assert "count" in data
    assert "first_3_titles" in data

    assert isinstance(data["count"], int)
    assert isinstance(data["first_3_titles"], list)