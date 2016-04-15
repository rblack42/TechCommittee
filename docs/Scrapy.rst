Fetching Data Using Scrapy
##########################

..  include::   /references.inc

Much of the data needed to feed the department website is already published on
the official ACC web site. Ideally, we should fetch this data from Datatel, but
that system is difficult to work with, and requires custom scripting to get at
the data we need. So, I am using Python Scrapy_ to fetch the data needed from
the published source. (This is the exact same data seen by the public).

Current Data
************

So far, the scripts access these data sets:

    * Course List by term

    * Staff list by deprtment

    * Class list by term

I also use this tool to extract a list of registered students for each class I
teach, and use the extracted data to set up the Excel spreadsheet I use as a
gradebook. All of this setup is automated. Further, I use a similar script to
generate the syllabus I use for each course. An example of the output from this
script is seen here:

    * `COSC 2325-001 Syllabus
      <http://www.co-pylit.org/classes/fall2015/cosc2325-001/syllabus/index.html#fall2015-cosc2325-001-syllabus>`_

Scraping Strategy
*****************

The process used at present involves downloading the web page and scraping that
page using the local copy, rather than scraping the live site directly. This
allows local testing, and makes sure the ACC server does not see high-speed
spider activity which might trigger security measures.

Installing Scrapy
=================

Assuming you are using virtualenv_ for Python development, this is how you get
Scrapy_ installed:

..  code-block:: text

    $ mkdir -p TechCommittee
    $ cd TechCommittee
    $ virtualenv _venv
    $ source _venv/bin/activate
    (_venv) $ pip install scrapy

Scrapy_ provides a few scripts to set up a web scraping project:

..  code-block:: text

    $ mkdir src
    $ cd src
    $ scrapy startproject ACCspider

This commands sets up a basic spider application with this structure:

..  code-block:: text

    ACCspider/
        |
        +- scrapy.cfg
        |
        +- ACCspider/
            |
            +- __init__.py
            |
            +- items.py
            |
            +- pipelines.py
            |
            +- settings.py
            |
            +- spiders/
                |
                +- __init__.py

Create Scrape Item Set
======================

Next, edit the ``items.py`` file to set up a data structure that will be filled in by the spider we will create:

..  literalinclude::   ../src/ACCspider/ACCspider/items.py
    :linenos:

Create the first Spider
=======================

Once we have the item class setup, it is time to create a simple spider that will access a data file, and verify that it cna be loaded for parsing. Here is the initial file:

..  literalinclude::    ../src/ACCspider/ACCspider/spiders/class_spider.py
    :linenos:

We can test this spider by runn in this command from project ``src`` directory:

..  code-block:: text

    $ scrapy crawl clist

IN this run, Scrapy_ will look into the ``spiders` folder and check for one with a name os ``clist``. IT will run that spider against the URL set listed. In this firt test, the page I am scraping has already been downloaded to my development system so I cna play with it without needing to hit the real ACC server repeatedly.



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

    
