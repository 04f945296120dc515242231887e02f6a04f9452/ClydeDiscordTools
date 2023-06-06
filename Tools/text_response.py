def text_response(message):
    """
    Generate a response to a text message based on a predefined set of triggers and responses.
    """
    # Define the triggers and responses
    trigger_response_map = {
        'hello': 'Hello there!',
        'how are you': 'I am doing well. Thank you for asking!',
        'goodbye': 'Goodbye!',
        'thank you': 'You are welcome!'
    }

    # Check if the message triggers a predefined response
    for trigger, response in trigger_response_map.items():
        if trigger in message.lower():
            return response

    # If no trigger is found, return a default response
    return 'I am sorry. I did not understand your message.'
