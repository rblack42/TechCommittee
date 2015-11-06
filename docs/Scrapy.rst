Fetching Data Using Scrapy
##########################

..  include::   /references.inc

Much of the data needed to feed the department website is already published on
the ACC web site. Ideally, we should fetch this data from Datatel, but that
system is difficult to work with, and requires custom scripting to get at the
data we need. So, I am using Python Scrapy_ to fetch the data needed from the
published source. (This is the exact same data seen by the public).

Current Data
************

So far, the scripts access these data sets:

    * Course List by term

    * Staff list by deprtment

    * Class list by term

Scraping Strategy
*****************

The process used at present involves downloading the web page and scraping that
page using the local copy, rather than scraping the live site directly. This
allows local testing, and makes sure the ACC server does not see high-speed
spider activity which might trigger security measures.

Data URLs
=========

The pages being processed are listed below:

Course List:
------------
    
    * Server: http://www3.austincc.edu
        
    * Path: /it/cms/www/catalog/coursedetails_fox.php
        
    * Query: year={{ year }}&deptcode={{ dept_code}}
    
        * Keys: 
            
            * year: 2016

            * dept_code: 
               
                * COSC

                * COIS 
            

Staff List
----------

    * Server: http://www6.austincc.edu
        
    * Path: /directory/search.php
        
    * Query: name=&campus=&dept={{ dept_code }}&position=&email=
            
        * Keys: 
                
            * dept_code:
            
                * COSC

                * COIS


There is overlap in these two pages

Class List by Term
------------------

    * Server: http://www6.austincc.edu

    * Path: /schedule/index.php
        
    * Query: op=browse&opclass=ViewSched&term={{ term }}&disciplineid={{ discipline_id }}&yr={{ year }}&ct=CC
        
        Keys:

            * Term: 216S000

            * discipline_id:

                * PCCOS

                * PCCIS
            
            * year 2016

Downloading Pages
*****************

Scrapy can download a web page and save it easily.
Here is an example script that can do this this:

..  code-block:: python

    import os
    import scrapy

    class Downloader(scrapy.Spider):

        def parse(self, response):
            with open(hash_url(response.url), 'w') as f:
                f.write(response.body)

To feed this script, you need to set up a list of URL patterns to scrape Scrapy_ will download and save each one.

Obviously, this needs work to make it more automatic.

URL List
========

Using the URL patterns found above, here is a snippet that sets up a list of URLs to fetch:

..  literalinclude::    ../src/URL.py
    :linenos:

    
