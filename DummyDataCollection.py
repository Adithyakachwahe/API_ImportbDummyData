import requests

# API endpoint URL
api_url = 'https://jsonplaceholder.typicode.com/posts/2'

# Make a GET request to the API endpoint
response = requests.get(api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON data from the response
    data = response.json()

    # Print the data
    print("Title:", data['title'])
    print("Body:", data['body'])
else:
    print(f"Error: {response.status_code}")
