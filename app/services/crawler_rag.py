import re

CRAWLED_PAGES = {}

def crawl_and_index(url: str):
    clean_url = url.rstrip("/")
    mock_content = (
        f"Official site content for {clean_url}: Erha Technologies provides intelligent workflow automations, "
        "next-generation RAG systems, and autonomous multi-agent software development meshes. "
        "Headquartered in Multan, our mission is to empower global operations through AI automation."
    )
    CRAWLED_PAGES[clean_url] = mock_content
    return len(mock_content.split())

def answer_from_website(url: str, query: str):
    clean_url = url.rstrip("/")
    if clean_url not in CRAWLED_PAGES:
        crawl_and_index(clean_url)
        
    content = CRAWLED_PAGES[clean_url]
    q_words = set(re.findall(r'\w+', query.lower()))
    c_words = set(re.findall(r'\w+', content.lower()))
    
    overlap = len(q_words.intersection(c_words))
    answer = f"According to {clean_url}: {content}"
    return answer, [f"{clean_url}#indexed-section-1"]
