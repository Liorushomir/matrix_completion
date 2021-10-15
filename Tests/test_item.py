import pytest
from items import Items


def test__init__create_item():
    genre_list = [0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0]
    exp = ["Action", "Adventure", "Comedy", "Fantasy", "Sci-Fi"]
    item = Items(None, None, None, None, None, genre_list)
    assert exp == item.genres
    print(True)

# ============================
# Fixtures
# ============================

@pytest.fixture
def genre_list():
    genre_list = ["unknown", "Action", "Adventure", "Animation",
                  "Children's", "Comedy", "Crime", "Documentary", "Drama", "Fantasy",
                  "Film-Noir", "Horror", "Musical", "Mystery", "Romance", "Sci-Fi",
                  "Thriller", "War", "Western"]
    return genre_list
