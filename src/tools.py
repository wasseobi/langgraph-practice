
import datetime


def what_time_is_it() -> str:
    """Get the current time.

    Returns:
        str: The current time in HH:MM:SS format.
    """

    return datetime.datetime.now().strftime("%H:%M:%S")


tools = [what_time_is_it]