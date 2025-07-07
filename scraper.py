import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0"
}

def search_imdb_movie(query):
    url = f"https://www.imdb.com/find?q={query.replace(' ', '+')}"
    print(f"[INFO] Searching IMDB: {url}")

    response = requests.get(url, headers=headers)
    print(f"[INFO] Status Code: {response.status_code}")

    if response.status_code != 200:
        print("[ERROR] IMDB returned an error page.")
        return None

    if "Are you a robot" in response.text:
        print("[ERROR] IMDB blocked the request with CAPTCHA.")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    # New IMDB search layout!
    result = soup.find('li', class_='ipc-metadata-list-summary-item')
    if result and result.a:
        href = result.a['href']
        print(f"[INFO] Found href: {href}")
        # Example: /title/tt4154796/?ref_=fn_al_tt_1
        parts = href.split('/')
        imdb_id = None
        for part in parts:
            if part.startswith('tt'):
                imdb_id = part
                break
        if imdb_id:
            return imdb_id

    print("[WARN] No results found in IMDB search page.")
    return None

def scrape_reviews(imdb_id):
    review_url = f"https://www.imdb.com/title/{imdb_id}/reviews"
    response = requests.get(review_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    review_divs = soup.find_all('div', class_='ipc-html-content-inner-div')
    
    reviews = []
    for div in review_divs:
        text = div.get_text(separator=' ', strip=True)
        reviews.append(text)
    return reviews
