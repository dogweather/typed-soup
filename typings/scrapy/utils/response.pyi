"""
This type stub file was generated by pyright.
"""

import scrapy
from typing import Any, Callable, Iterable, Tuple, Union
from weakref import WeakKeyDictionary
from twisted.web import http
from w3lib import html
from scrapy.http.response import Response
from scrapy.utils.decorators import deprecated

"""
This module provides some useful functions for working with
scrapy.http.Response objects
"""
_baseurl_cache: WeakKeyDictionary[Response, str] = ...
def get_base_url(response: scrapy.http.response.text.TextResponse) -> str:
    """Return the base url of the given response, joined with the response url"""
    ...

_metaref_cache: WeakKeyDictionary[Response, Union[Tuple[None, None], Tuple[float, str]]] = ...
def get_meta_refresh(response: scrapy.http.response.text.TextResponse, ignore_tags: Iterable[str] = ...) -> Union[Tuple[None, None], Tuple[float, str]]:
    """Parse the http-equiv refresh parameter from the given response"""
    ...

def response_status_message(status: Union[bytes, float, int, str]) -> str:
    """Return status code plus status text descriptive message"""
    ...

@deprecated
def response_httprepr(response: Response) -> bytes:
    """Return raw HTTP representation (as bytes) of the given response. This
    is provided only for reference, since it's not the exact stream of bytes
    that was received (that's not exposed by Twisted).
    """
    ...

def open_in_browser(response: Union[scrapy.http.response.html.HtmlResponse, scrapy.http.response.text.TextResponse,], _openfunc: Callable[[str], Any] = ...) -> Any:
    """Open *response* in a local web browser, adjusting the `base tag`_ for
    external links to work, e.g. so that images and styles are displayed.

    .. _base tag: https://www.w3schools.com/tags/tag_base.asp

    For example:

    .. code-block:: python

        from scrapy.utils.response import open_in_browser


        def parse_details(self, response):
            if "item name" not in response.body:
                open_in_browser(response)
    """
    ...

