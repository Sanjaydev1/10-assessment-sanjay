from api_utils import fetch_posts


def test_fetch_posts():
    result = fetch_posts(1)

    assert "count" in result
    assert "first_3_titles" in result

    assert isinstance(result["count"], int)
    assert isinstance(result["first_3_titles"], list)