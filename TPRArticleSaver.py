import requests
from bs4 import BeautifulSoup
import os
import threading
import time
from xml.etree import ElementTree
from urllib.parse import urlparse


# Function to get URLs from the sitemap
def get_sitemap_urls(sitemap_url):
    response = requests.get(sitemap_url)
    tree = ElementTree.fromstring(response.content)
    urls = [url.text for url in tree.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
    return urls

# Helper function to print a message every 30 seconds
def print_message_every_30_seconds():
    global keep_printing
    while keep_printing:
        print("Program is running...")
        time.sleep(30)

# Helper function to get the content of a web page
def get_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

# Deprecated helper function to get all links on the issues page
# def get_issue_link(issues_url):
#     soup = get_soup(issues_url)
#     issues_links = []
#     for h3 in soup.find_all('h3'):
#         a = h3.find('a', href=True)
#         if a and a['href'].startswith('http'):
#             issues_links.append(a['href'])
#     return issues_links

# Deprecated helper function to get all links to articles on a page
# def get_article_links(issue_url):
#     soup = get_soup(issue_url)
#     articles = []
#     for ul in soup.find_all('ul'):
#         for a in ul.find_all('a', href=True):  # Iterating over each anchor tag
#             if a['href'].startswith('http'):
#                 articles.append(a['href'])
#     return articles


# Helper function to save the text of the articles in a text file
def save_article(article_url, folder='articles'):
    try:
        soup = get_soup(article_url)

        # Find the title
        title_tag = soup.find('h1', class_='entry-title')
        title = title_tag.get_text(strip=True) if title_tag else 'No Title'

        # Find the author info
        author_info_tag = title_tag.find_next_sibling('p') if title_tag else None
        author_info = author_info_tag.get_text(strip=True) if author_info_tag else 'No Author Info'

        # Find the article content
        article_content_tag = soup.find('div', class_='entry-content')
        article_content = article_content_tag.get_text(strip=True) if article_content_tag else 'No Content'

        # Build an entry
        full_article = f"Title: {title}\nAuthor: {author_info}\n\n{article_content}"

        # Generate a more unique filename
        parsed_url = urlparse(article_url)
        filename = '-'.join(parsed_url.path.strip('/').split('/')) + '.txt'
        filepath = os.path.join(folder, filename)

        os.makedirs(folder, exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(full_article)
        print(f"Saved: {filename}")
    except Exception as e:
        print(f"Error processing {article_url}: {e}")


#Main
# issues_url = 'https://thepeerreview-iwca.org/issues/'
# issues_links = get_issue_link(issues_url)
# for issue_link in issues_links:
#     article_links = get_article_links(issue_link)
#     for article_link in article_links:
#         save_article(article_link)

if __name__ == "__main__":
    keep_printing = True
    message_thread = threading.Thread(target=print_message_every_30_seconds)
    message_thread.start()

    # Fetch article URLs from the sitemap
    sitemap_url = 'https://thepeerreview-iwca.org/sitemap-1.xml'
    article_urls = get_sitemap_urls(sitemap_url)

    for article_url in article_urls:
        print(article_url)
        save_article(article_url)

    keep_printing = False
    message_thread.join()
    print("Complete")