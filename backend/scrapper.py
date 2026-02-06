import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(url: str):
    headers = {
        "User-Agent": "WikiQuizBot/1.0 (Educational Project)"
    }

    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            return {"error": f"Failed to fetch page. Status code: {response.status_code}"}
        
        soup = BeautifulSoup(response.text, 'html.parser')

        # Check if h1 element exists before accessing .text
        title_element = soup.find("h1")
        if not title_element:
            return {"error": "Article title not found - no h1 element"}
        
        # Get title text and check if it's empty
        title = title_element.text.strip()
        if not title:
            return {"error": "Article title is empty"}
        
        # Find all paragraphs
        paragraphs = soup.find_all("p")
        
        # Check if paragraphs list is empty
        if not paragraphs:
            return {"error": "Article is empty - no paragraphs found"}
        
        # Join paragraph texts and filter out empty ones
        content = " ".join([p.text.strip() for p in paragraphs if p.text.strip()])
        
        # Check if content is empty after joining
        if not content:
            return {"error": "Article content is empty - all paragraphs are empty"}
        
        return {
            "title": title,
            "content": content
        }
    
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}