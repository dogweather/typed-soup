"""
This type stub file was generated by pyright.
"""

from typing import Optional, TYPE_CHECKING
from twisted.internet.defer import Deferred
from scrapy.http.request import Request
from scrapy.settings import BaseSettings
from scrapy.spiders import Spider
from scrapy.utils.request import RequestFingerprinterProtocol
from typing_extensions import Self
from scrapy.crawler import Crawler

if TYPE_CHECKING:
    ...
class BaseDupeFilter:
    @classmethod
    def from_settings(cls, settings: BaseSettings) -> Self:
        ...
    
    def request_seen(self, request: Request) -> bool:
        ...
    
    def open(self) -> Optional[Deferred]:
        ...
    
    def close(self, reason: str) -> Optional[Deferred]:
        ...
    
    def log(self, request: Request, spider: Spider) -> None:
        """Log that a request has been filtered"""
        ...
    


class RFPDupeFilter(BaseDupeFilter):
    """Request Fingerprint duplicates filter"""
    def __init__(self, path: Optional[str] = ..., debug: bool = ..., *, fingerprinter: Optional[RequestFingerprinterProtocol] = ...) -> None:
        ...
    
    @classmethod
    def from_settings(cls, settings: BaseSettings, *, fingerprinter: Optional[RequestFingerprinterProtocol] = ...) -> Self:
        ...
    
    @classmethod
    def from_crawler(cls, crawler: Crawler) -> Self:
        ...
    
    def request_seen(self, request: Request) -> bool:
        ...
    
    def request_fingerprint(self, request: Request) -> str:
        ...
    
    def close(self, reason: str) -> None:
        ...
    
    def log(self, request: Request, spider: Spider) -> None:
        ...
    


