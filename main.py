import requests
import json  # unused import — AI Teammate can flag this
import math  # unused import

def calculate_average(numbers):
    if not numbers:
        return 0
    # Intentional inefficiency: manually summing instead of using sum()
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)

def process_user_data(user):
    # Intentional bug: should check for 'email', not 'mail'
    if 'mail' not in user:
        raise ValueError("Missing email field")
    # Style issue: unnecessary f-string concatenation
    result = f"User {user['name']}" + " processed."
    return result

def fetch_data(url):
    response = requests.get(url)
    if response.status_code != 200:
        # Missing exception handling
        print("Warning: non-200 status code", response.status_code)
    return response.json()

def unused_function():
    # Dead code — never called
    print("This function is not used.")

def divide(a, b):
    return a / b  # No zero-division check

