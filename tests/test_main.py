import pytest
from main import calculate_average, process_user_data, fetch_data

def test_calculate_average_normal_case():
    assert calculate_average([1, 2, 3]) == 2

def test_calculate_average_empty_list():
    assert calculate_average([]) == 0

def test_process_user_data_valid():
    user = {"name": "Alice", "email": "alice@example.com"}
    # This will fail due to bug ('mail' instead of 'email')
    assert process_user_data(user) == "User Alice processed."

def test_process_user_data_missing_field():
    with pytest.raises(ValueError):
        process_user_data({"name": "Bob"})

def test_will_fail():
    assert 1 + 1 == 3  # intentional failure


@pytest.mark.skip(reason="Skipping network request test for demo")
def test_fetch_data_real_request():
    assert fetch_data("https://jsonplaceholder.typicode.com/todos/1")["id"] == 1
