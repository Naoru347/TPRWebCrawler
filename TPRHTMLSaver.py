import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urlparse
import xml.etree.ElementTree as ET

def get_soup(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.content, 'html.parser')
    return None

def save_html(url, folder='html_pages'):
    soup = get_soup(url)
    if soup is not None:
        parsed_url = urlparse(url)
        filename = parsed_url.netloc + parsed_url.path
        filename = filename.replace('/', '_').strip('_') + '.html'
        filepath = os.path.join(folder, filename)
        os.makedirs(folder, exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(str(soup))

def get_urls_from_sitemap(sitemap_url):
    response = requests.get(sitemap_url)
    urls = []
    if response.status_code == 200:
        sitemap_xml = response.content
        root = ET.fromstring(sitemap_xml)
        namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        for sitemap in root.findall('ns:url', namespace):
            url = sitemap.find('ns:loc', namespace).text
            urls.append(url)
    return urls

def main():
    sitemap_url = 'https://thepeerreview-iwca.org/sitemap-1.xml'
    urls = get_urls_from_sitemap(sitemap_url)

    for url in urls:
        print(f"Visiting: {url}")
        save_html(url)

if __name__ == "__main__":
    main()
