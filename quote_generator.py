import requests

def generate_quote():
    """
    Generate a random quote using the ZenQuotes API.
    """
    # Define the API endpoint and send a request
    endpoint = 'https://zenquotes.io/api/random'
    response = requests.get(endpoint).json()[0]

    # Parse the response and return the quote
    author = response['a']
    quote = response['q']
    return f'"{quote}" - {author}'
