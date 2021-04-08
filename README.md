# Web-crawling using Scrapy

## Description:
This project uses Scrapy- a python framework for large scale web scraping- to scrape the titles of ![Solar Energy Project Portfolio](https://coronalenergy.com/solar-portfolio/?tag=Utility%20Scale) currently existing in the US and transferring the extracted data into a CSV file that can be used for further data manipulation. The motivation for this project is to create a database for the portfolio of all existing projects in Massachusetts that is easily accessible for further data analysis. However, given the time limitation and restriction on the scope of the project this project focuses on the small element of the final goal. The script scraped a single webpage, extracted the solar project titles and compiled those in a csv file. Since the project uses pre-existing module, it comes with inbuilt components that we briefly discuss in this readme. 
<br>
<br>
* Items: Scrapy provides the Item class for this purpose. Item objects are simple containers used to collect the scraped data. They provide a dictionary-like API with a convenient syntax for declaring their available fields. ![Scrapy Documentation](https://docs.scrapy.org/en/0.24/topics/items.html)
* Pipeline: For this project, item pipeline is not required but as it expands item pipeline cleanses HTML data. validates scraped data, and look for duplicates (and dropping them)
* FinalProject: This is the main .py file that builds the spider using css selector.
* Settings: For this project, this file is used to export the items into a csv file. The Scrapy settings allows you to customize the behaviour of all Scrapy components, including the core, extensions, pipelines and spiders themselves.
* Middlewares: The spider middleware is a framework of hooks into Scrapy's spider processing mechanism where you can plug custom functionality to process the responses that are sent to Spiders for processing and to process the requests and items that are generated from spiders. But this project doesn't modify middlewares.

## Challenges:
<br>
<br>
* One of the challenges faced was in extracting multiple attributes of the frame block. I tried multiple ways to solve it; one is to use multiple loops and other method was defining the extractors outside the loop and then creating a dictionary inside that takes in the values from the extractors but for now none of these methods worked. 
* The data attributes of the title are embedded in the subclass(li) of the main class -div, and li- the subclass- has another class div that holds the value of the title. I'm planning on spending more time on it after the submission to solve this problem and scrape the details.



