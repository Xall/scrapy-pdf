Scrapy PDF
==========
This project recursively finds all links to pdfs on a website (+subdomains) and exports them as a csv file

Usage
=====
scrapy crawl pdfs -o items.csv -t csv

Changelog
=========
1.0 First working draft

Notes // TODO
=============

* restrict to subfolders

    allowed_domains = ["www.uni-ulm.de"]
    start_urls = ["http://www.uni-ulm.de/einrichtungen/assist.html"]

    rules = (
        Rule(LinkExtractor(allow=('einrichtungen\/assist')), callback="parse_items", follow= True),
    )

* generate a nice html with download link (or download while scraping and add local link)