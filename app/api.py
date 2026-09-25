from fastapi import FastAPI
from app.config import settings
from app.models import CrawlRequest, WebsiteQueryRequest, WebsiteAnswerResponse
from app.services.crawler_rag import crawl_and_index, answer_from_website

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

@app.post("/crawl")
def crawl(req: CrawlRequest):
    words_indexed = crawl_and_index(req.url)
    return {"status": "indexed", "url": req.url, "words_indexed": words_indexed}

@app.post("/query", response_model=WebsiteAnswerResponse)
def query_site(req: WebsiteQueryRequest):
    ans, sources = answer_from_website(req.url, req.query)
    return WebsiteAnswerResponse(url=req.url, query=req.query, answer=ans, sources=sources)
