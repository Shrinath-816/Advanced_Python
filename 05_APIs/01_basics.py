# Import the requests library.
# It is used to send HTTP requests (GET, POST, PUT, DELETE, etc.)
# to interact with REST APIs.
import requests


# URL of the Pokémon REST API endpoint.
# This endpoint returns information about Pokémon in JSON format.
url = "https://pokeapi.co/api/v2/pokemon"


# Send an HTTP GET request to the API.
# The server responds with a Response object containing:
# - Status code (200, 404, etc.)
# - Headers
# - Response body
response = requests.get(url)


# Convert the JSON response into a Python dictionary.
# JSON -> Python Dictionary
#
# Example:
# {
#     "count": ...,
#     "next": ...,
#     "previous": ...,
#     "results": [...]
# }
data = response.json()


# Print the complete response received from the API.
print(data)