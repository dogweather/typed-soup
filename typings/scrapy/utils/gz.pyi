"""
This type stub file was generated by pyright.
"""

from scrapy.http import Response

def gunzip(data: bytes, *, max_size: int = ...) -> bytes:
    """Gunzip the given data and return as much data as possible.

    This is resilient to CRC checksum errors.
    """
    ...

def gzip_magic_number(response: Response) -> bool:
    ...

