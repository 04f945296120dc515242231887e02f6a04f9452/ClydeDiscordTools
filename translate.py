import requests


def translate(text, source_language, target_language):
    """
    Translate text from one language to another using the Yandex.Translate API.
    """
    # Define the API endpoint and request parameters
    endpoint = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    params = {
        'text': text,
        'lang': f'{source_language}-{target_language}',
        'key': 'trnsl.1.1.20220607T011741Z.75c7c99a9e3de90e.8d7b5d2554dc604ae43b2bfe9d9a7a7b8a6cb6dd'
    }

    # Send a request to the API and parse the response
    response = requests.get(endpoint, params=params).json()
    if response['code'] != 200:
        raise Exception(response['message'])
    translated_text = response['text'][0]

    return translated_text
