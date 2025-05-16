# -*- coding: utf-8 -*-
import scrapy
import pandas as pd

# read the csv with all of the urls
trails = trails = pd.read_csv('C:/Users/dylan/Downloads/wta_parks_data - wta_parks_data (1).tsv',sep='\t')
 
# Import the CrawlerProcess: for running the spider
from scrapy.crawler import CrawlerProcess
 
# Create the Spider class
class WTA_rating_spider(scrapy.Spider):
  name = "wta_rating_spider"
  # start_requests method
  def start_requests(self):
    for url in links_to_follow:
        yield scrapy.Request(url = url, callback = self.parse)

      
  # Second parsing method
  def parse(self, response):
    #Get trail title information
    title = response.css(' h1.documentFirstHeading::text')
    title_ext = title.extract_first()
    
    #Get trail rating information
    rating = response.css(' div.current-rating::text')
    rating_ext = rating.extract_first()[0:3]
    
    #Get trail votes information
    votes = response.css(' div.rating-count::text')
    votes_ext = votes.extract_first()[1:6]
    
    #append onto the current ratings database
    rating_df.append([title_ext,rating_ext,votes_ext])
 
# Initialize the dictionary **outside** of the Spider class
rating_df = []
links_to_follow = trails['url']

# Run the Spider
process = CrawlerProcess()
process.crawl(WTA_rating_spider)
process.start()

#Convert dictionary into dataframe
rating_df = pd.DataFrame(rating_df)

# Print a preview of courses
