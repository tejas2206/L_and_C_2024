import requests
import json
import re
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def fetch_tumblr_blog_info(blog_name, start, end):
    try:
        if start < 1 or end < start:
            print("Invalid range. Please enter a valid range.")
            return

        url = f"https://{blog_name}.tumblr.com/api/read/json?type=photo&num={end - start + 1}&start={start - 1}"

        session = requests.Session()
        retries = Retry(
            total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504]
        )
        session.mount("https://", HTTPAdapter(max_retries=retries))

        # Making GET request to the Tumblr API with timeout
        response = session.get(url, timeout=10)

        if response.status_code != 200:
            print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
            return

        match = re.search(r"var tumblr_api_read = (.*);$", response.text)
        if not match:
            print("Failed to extract JSON data from response.")
            return

        data = json.loads(match.group(1))

        blog_info = data["tumblelog"]
        title = blog_info.get("title", "N/A")
        description = blog_info.get("description", "N/A")
        name = blog_info.get("name", "N/A")
        total_posts = data.get("posts-total", "N/A")

        print(f"title: {title}")
        print(f"name: {name}")
        print(f"description: {description}")
        print(f"no of post: {total_posts}\n")

        posts = data["posts"]
        for index, post in enumerate(posts, start=start):
            if "photos" in post:
                for photo in post["photos"]:
                    photo_url = photo["photo-url-1280"]
                    print(f"{index}. {photo_url}")

    except requests.exceptions.Timeout:
        print("Request timed out. Please try again later.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

blog_name = input("Enter the Tumblr blog name: ").strip()
range_input = input("Enter the range (start-end): ").strip()

try:
    start, end = map(int, range_input.split("-"))
    fetch_tumblr_blog_info(blog_name, start, end)
except ValueError:
    print("Invalid input format for range. Please enter in start-end format.")