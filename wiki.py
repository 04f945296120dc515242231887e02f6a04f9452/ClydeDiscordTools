import wikipedia


def search_wikipedia(query):
    """
    Search for a topic on Wikipedia and return a summary of the page.
    """
    try:
        page = wikipedia.page(query)
        summary = wikipedia.summary(query, sentences=2)
        return f'{page.title}\n\n{summary}'
    except wikipedia.exceptions.PageError as e:
        return 'Page not found.'
    except wikipedia.exceptions.DisambiguationError as e:
        return 'Ambiguous search term. Please be more specific.' 
