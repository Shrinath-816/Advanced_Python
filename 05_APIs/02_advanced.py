# Import the requests library to make HTTP requests to REST APIs.
import requests


# Base URL of the Pokémon API.
url = "https://pokeapi.co/api/v2/pokemon"


# Send an initial request to get the total number of Pokémon records.
response = requests.get(url)

# Extract the value of the "count" field from the JSON response.
# .get("count") safely returns the value associated with the key "count".
total_records = response.json().get("count")

print(total_records)


# List to store the response from each paginated API request.
all_data = []


# Fetch all Pokémon data page by page.
#
# offset -> Starting index of records to fetch.
# limit  -> Number of records returned per request.
#
# Here, every API call fetches 20 Pokémon.
for i in range(0, total_records, 20):

    # Construct the paginated URL dynamically.
    paginated_url = f"{url}?offset={i}&limit=20"

    # Send the GET request for the current page.
    response = requests.get(paginated_url)

    # Convert the JSON response into a Python dictionary.
    data = response.json()

    # Store the current page's response in the list.
    all_data.append(data)


# Print the total number of API responses (pages) collected.
print(len(all_data))