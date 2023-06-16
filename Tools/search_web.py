import requests

def search_web(query):
    """
    Search the web for a given query using the DuckDuckGo API.
    """
    # Base URL for the DuckDuckGo Instant Answer API
    base_url = 'https://api.duckduckgo.com/'

    # Set URL parameters
    params = {
        'q': query,
        'format': 'json'
    }

    # Send GET request to the API
    response = requests.get(base_url, params=params)

    # Extract the abstract from the API response
    abstract = response.json()['Abstract']

    # Return the abstract
    return abstract
