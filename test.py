import requests
import json

# Replace with your actual Copilot API key and endpoint
COPILOT_API_KEY = "8248796bddec49d2b267eaa6d9dd4ade.fad3c71c2bb3f0d0"
COPILOT_API_URL = "https://api.copilot.com/v1/send-message"

# Function to call Copilot API
def filter_locations_via_copilot(text):
    headers = {
        "Authorization": f"Bearer {COPILOT_API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Prompt telling Copilot what to do
    data = {
        "prompt": f"Extract all the location names and addreses from the following text:\n\n{text}"
    }

    try:
        # Send request to Copilot API
        response = requests.post(COPILOT_API_URL, json=data, headers=headers)
        response.raise_for_status()  # Raise an error if the HTTP response is bad
        response_data = response.json()

        # Assuming the API returns locations in a field named 'locations'
        locations = response_data.get("locations", [])
        return locations

    except requests.RequestException as e:
        print(f"Error calling Copilot API: {e}")
        return []

# Sample transcription text
sample_text = """
I recently visited New York City and stayed at the Hilton Midtown. We walked down 5th Avenue and visited the Empire State Building at 350 5th Avenue, New York, NY 10118.
Later, we traveled to Paris and saw the Eiffel Tower located at Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France.
"""

# Calling the API to filter locations
locations = filter_locations_via_copilot(sample_text)

# Output the extracted locations
if locations:
    print("Extracted Locations:")
    for location in locations:
        print(location)
else:
    print("No locations found.")
