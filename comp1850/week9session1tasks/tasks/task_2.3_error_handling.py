"""
Task 2.3: Handle Errors in API Requests

Goal: Learn to handle common API errors including 404s, timeouts, and invalid JSON.

Exercises:
- Handle 404 errors
- Handle timeout errors
- Handle invalid JSON responses
"""

import httpx
import json

# Exercise 3.1: Handle 404 errors
url = "https://jsonplaceholder.typicode.com/posts/9999"
# TODO: Send GET request and handle 404 error
try:
    response = httpx.get(url)
    response.raise_for_status()  
    data = response.json()
    print("404 Exercise: Request successful, data:", data)
except httpx.HTTPStatusError as e:
    if e.response.status_code == 404:
        print("404 Exercise: Resource not found (404 error handled)")
    else:
        print(f"404 Exercise: HTTP error occurred: {e}")
except Exception as e:
    print(f"404 Exercise: Unexpected error: {e}")


# Exercise 3.2: Handle timeout errors
# TODO: Send GET request with a very short timeout and catch timeout exception
try:
    response = httpx.get(url, timeout=0.001)  
    data = response.json()
    print("Timeout Exercise: Request successful, data count:", len(data))
except httpx.TimeoutException:
    print("Timeout Exercise: Request timed out (timeout error handled)")
except Exception as e:
    print(f"Timeout Exercise: Unexpected error: {e}")

# Exercise 3.3: Handle invalid JSON responses
url = "https://jsonplaceholder.typicode.com/posts"
# TODO: Try parsing JSON and handle invalid JSON errors
try:
    response = httpx.get(url)
    response.raise_for_status()
    invalid_json = response.text.replace('"', '')  
    data = json.loads(invalid_json)
    print("Invalid JSON Exercise: Parsing successful, data:", data)
except json.JSONDecodeError:
    print("Invalid JSON Exercise: Invalid JSON response (JSON error handled)")
except httpx.HTTPStatusError as e:
    print(f"Invalid JSON Exercise: HTTP error occurred: {e}")
except Exception as e:
    print(f"Invalid JSON Exercise: Unexpected error: {e}")