from pydantic import BaseModel, HttpUrl
from typing import List

class CrawlRequest(BaseModel):
    url: str
    max_pages: int = 5

class WebsiteQueryRequest(BaseModel):
    url: str
    query: str

class WebsiteAnswerResponse(BaseModel):
    url: str
    query: str
    answer: str
    sources: List[str]
