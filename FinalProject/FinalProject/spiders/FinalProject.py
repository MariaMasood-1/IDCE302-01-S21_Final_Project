# Created by: Maria Masood
# Date: 04/07/2021
# Description: built a spider to scrape the https://coronalenergy.com/solar-portfolio/?tag=Utility%20Scale to get
#the list of solar projects in United states


#importing libraries
import scrapy
from ..items import FinalprojectItem

class Final_Project(scrapy.Spider):  #inheriting from already written class in spider
    name = 'projects'
    start_urls = [
        'https://coronalenergy.com/solar-portfolio/?tag=Utility%20Scale'
    ]

    # give a list of url that we want to scrape
    # the class spider that we inherit expect two variable assignment that is name and url
    def parse(self, response):  #parse is called whenever the crawler(spider) has successfully crawled the url

        items = FinalprojectItem()

        content_information = response.css('div.col.col-1')
        for data in content_information:    #looping for all the title values

            title = data.css('h4.textdiv_title::text').extract()  #extracting title from the url using css selectors



            items['title'] = title


            yield items      #the source code from the url will be held in response. response contains the source code of our website

