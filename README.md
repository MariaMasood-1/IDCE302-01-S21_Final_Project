# Script 1:

This script scrapes the 5-day weather forecast from the National Weather Service website and extracts information from detailed forecasts listed under the forecast-tombstone class name using the BeautifulSoup library. Web-scraping is a tool used for extracting the content off the website with the help of bot or spiders. This tool scrapes the underlying HTML code along with the data stored in that code. 
Libraries used
<br>

* requests: Requests allows you to send organic, grass-fed HTTP/1.1 requests, without the need for manual labor.
 
* bs4: The official name of PiP's Beautiful Soup Python package is beautifulsoup4. This package ensures that if you type pip install bs4 by mistake you will end up with Beautiful Soup. Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree
<br> 
This code ran very smoothly on the first run. Since we are taking input from the user, it is important to note that the user input is in integer but the argument passed through the url is string type. 
For the formatting of the code I used the .replace() function to manually alter different parameters, for example replacing ThursdayNight with Thursday Night. I was looking for a more efficient way of adding space in the text. The difficulty I faced was in assigning an index for the desired operation to manipulate the string.
I’m trying to learn more about web-scraping through other avenues including the ethics and regulations of web scraping. I tried building a web crawler for my final project to extract the information about solar projects in Massachusetts.
<br>
<br>
 
# Script 2:
<br>

## Web-crawling using Scrapy

### Description:
This project uses Scrapy- a python framework for large scale web scraping- to scrape the titles of ![Solar Energy Project Portfolio](https://coronalenergy.com/solar-portfolio/?tag=Utility%20Scale) currently existing in the US and transferring the extracted data into a CSV file that can be used for further data manipulation. The motivation for this project is to create a database for the portfolio of all existing projects in Massachusetts that is easily accessible for further data analysis. However, given the time limitation and restriction on the scope of the project, this project focuses on the small element of the final goal. The script scraped a single webpage, extracted the solar project titles and compiled those in a csv file. Since the project uses pre-existing module, it comes with inbuilt components that we briefly discuss in this readme. The goal of this project was also to learn the implementation of scrapy for future projects. 
### **To run the file:**
<br>
* downloading the whole folder. <br>
* cd FinalProject <br>
* type 'scrapy crawl projects' in the terminal**  <br>
* There should be a projects.csv file in the Final Project <br>
<br>
<br>
### Elements of the script: <br>
* Items: Scrapy provides the Item class for this purpose. Item objects are simple containers used to collect the scraped data. They provide a dictionary-like API with a convenient syntax for declaring their available fields. ![Scrapy Documentation](https://docs.scrapy.org/en/0.24/topics/items.html)
* Pipeline: For this project, item pipeline is not required but as it expands item pipeline cleanses HTML data. validates scraped data, and look for duplicates (and dropping them)
* FinalProject: This is the main .py file that builds the spider using css selector to extract the titles from the webpage.
* Settings: For this project, this file is used to export the items into a csv file. The Scrapy settings allows you to customize the behaviour of all Scrapy components, including the core, extensions, pipelines and spiders themselves.
* Middlewares: This is a framework of hooks into Scrapy's spider processing mechanism where you can plug custom functionality to process the responses that are sent to Spiders for processing. But this project doesn't modify middlewares.

### Challenges:
<br>

* One of the challenges faced was in extracting multiple attributes of the frame block. I tried multiple ways to solve it; one is to use multiple loops and other method was defining the extractors outside the loop and then creating a dictionary inside that takes in the values from the extractors but for now none of these methods worked. 
* The data attributes of the 'title' are embedded in the subclass(li) of the main class -div, and li(the subclass) has its own class div that holds the value of the title. I'm planning on spending more time on it after the submission to solve this problem and scrape the details.



