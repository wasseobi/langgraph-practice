import datetime

from langchain_google_community import GoogleSearchAPIWrapper

def what_time_is_it() -> str:
    """Get the current time.

    Returns:
        str: The current time in HH:MM:SS format.
    """

    return datetime.datetime.now().strftime("%H:%M:%S")

def google_search(topic: str, num_results: int) -> list:
    """
    Perform a Google search and retrieve the results.

    Args:
        topic (str): The search query.
        num_results (int): The number of search results to retrieve.

    Returns:
        list: A list of search results.
    """
    search = GoogleSearchAPIWrapper()
    results = []

    res = search.results(topic, num_results=num_results)
    results.extend(res)

    return results


tools = [what_time_is_it, google_search]