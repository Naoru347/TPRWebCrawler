TPRWebCrawler
Overview

TPRWebCrawler is a collection of Python scripts designed to automate the extraction and saving of articles and HTML source code from The Peer Review (TPR) website. This project consists of three main scripts:

    TPRArticleSaver.py: Saves articles from the website as text files.
    TPRHTMLSaver.py: Downloads and saves the HTML source code of web pages.
    TPRWebCrawler.py: A master script that runs both the Article Saver and HTML Saver scripts sequentially.

Prerequisites

    Python 3.x
    Libraries: requests, bs4 (BeautifulSoup4), lxml

Installation

    Clone the Repository

    bash

git clone [repository URL]

Install Required Libraries

bash

    pip install requests bs4 lxml

Usage
Running TPRWebCrawler.py

This script combines the functionality of both the TPRArticleSaver and TPRHTMLSaver scripts. To execute, navigate to the directory containing the scripts and run:

bash

python TPRWebCrawler.py

Individual Script Usage

To run the scripts individually:

    TPRArticleSaver.py:

    bash

python TPRArticleSaver.py

TPRHTMLSaver.py:

bash

    python TPRHTMLSaver.py

Output

    Articles will be saved in the articles folder.
    HTML source code will be saved in the html folder.

Customization

You can modify the scripts to suit different requirements, such as changing the URLs, adjusting the parsing logic, or modifying the output file format and location.
Troubleshooting

If you encounter issues:

    Ensure all dependencies are installed.
    Check your Python version.
    Confirm the scripts' access to the internet.

Contributing

Contributions to TPRWebCrawler are welcome. Please follow the standard fork-pull request workflow.
License

[Specify the license under which your project is released]
Contact

For support or queries, please [contact information or link to issue tracker].
