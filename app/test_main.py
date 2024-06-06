from app.main import get_human_age


def test_get_human_age() -> None:
    test_data = [
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ]

    for cat_age, dog_age, result in test_data:
        assert get_human_age(cat_age, dog_age) == result
