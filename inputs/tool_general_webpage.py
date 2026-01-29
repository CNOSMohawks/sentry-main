"""
DATE
    12.07.25

DESCRIPTION
    Toolsets for general webpage parsing and utilization; for example,
    downloading the HTML data of a page; or reading a PDF hosted on a
    specific URL.
"""

# @TODO: we **must** use aiohttp and other async functions for the need of speed.

import aiohttp

async def download_url_data(url: str) -> str:
    """Given a `url`, download the data from that webpage and return
    the HTML contents.

    Args:
        url: A string representing the webpage URL.
    
    Returns:
        string: A string with all the webpage data. Returns empty if nothing was found.
    """
    return ""

async def download_url_data_bulk(urls: list[str]) -> list[str]:
    """
    Given a list of `url`, download all the data from those webpages
    and return their HTML contents.

    Args:
        urls: A `list` of webpage URLs.

    Returns:
        list: A list with HTML data of the respective input URLs. Returns empty(for that specific URL), if nothing was found.
    """
    data = [""] * len(urls)
    return data