import requests
from bs4 import BeautifulSoup
import os

# Helper function to get the content of a web page
def get_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

# Helper function to get all links on the issues page
def get_issue_link(issues_url):
    soup = get_soup(issues_url)
    issues_links = []
    for h3 in soup.find_all('h3'):
        a = h3.find('a', href=True)
        if a and a['href'].startswith('http'):
            issues_links.appened(a['href'])
    return issues_links

# Helper function to get all links to articles on a page
def get_article_links(issues_url):
    soup = get_soup(issues_url)
    articles = []
    for ul in soup.find_all('ul'):
        a = ul.find.all('a', href=True)
        if a['href'].startswith('http'):
            articles.append(a['href'])
    return articles

# Helper function to save the text of the articles in a text file
def save_article(article_url, folder='articles'):
    