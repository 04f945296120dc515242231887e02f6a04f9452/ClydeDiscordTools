import requests
import json


def report_user(user_id):
    """
    Report a Discord user to Trust and Safety.
    """
    # Define the API endpoint and headers
    endpoint = 'https://discord.com/api/v9/report'
    headers = {
        'Authorization': 'Bot YOUR_BOT_TOKEN_HERE',
        'Content-Type': 'application/json'
    }

    # Define the report data
    payload = {
        'channel_id': None,
        'guild_id': None,
        'message_id': None,
        'user_id': user_id,
        'reason': 'Spam or other harmful content',
        'evidence': 'User has been sending unsolicited messages to multiple servers'
    }

    # Send a POST request to the API and parse the response
    response = requests.post(endpoint, headers=headers, data=json.dumps(payload))
    if response.status_code != 201:
        raise Exception('Failed to report user: ' + response.text)

    return 'User reported to Trust and Safety.'
