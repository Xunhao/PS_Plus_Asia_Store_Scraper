#!/usr/bin/env python
# coding: utf-8

# # PS Store Asia scrapper

# In[1]:


from bs4 import BeautifulSoup
import requests
import csv


# In[3]:


# Create a csv file with the required columns to store the scraped data 

# newline = '' to avoid having a blank row inserted after each writerow
# encoding = 'utf-8' to avoid encoding issue
# insert your preferred directory
csv_file = open('Discounted_PS4_games.csv', 'w', newline = '', encoding = 'utf-8')

csv_writer = csv.writer(csv_file)

# Writing the necessary column headers 
csv_writer.writerow(['title', 'original_price', 'discounted_price', 'percentage_saved'])


# In[2]:


# This part is crucial in creating the code to identify the maximum number of pages

# request library is common for making HTTP request in Python
source = requests.get('https://store.playstation.com/en-sg/grid/STORE-MSF86012-SPECIALOFFER/1?gameContentType=games&platform=ps4').text

# BS documentation recommends using lxml parser library for speed
soup = BeautifulSoup(source, 'lxml') 

# use soup.prettify() if you wish to examine the html code


# ## What information do we wish to scrap?
# 
# 1) Game title
# 
# 2) Original Price
# 
# 3) Price after discount
# 
# 4) Percentage saved
# 
# We will be scraping (1), (2), (3) from the website while calculating (4) separately

# In[5]:


# Identify the max number of pages with discounted items

# Notice that the link for the last page is always at the end
# The maximum number of page can be found inside the link before '?'
# Example of the link /en-sg/grid/STORE-MSF86012-SPECIALOFFER/6?gameContentType=games&platform=ps4
# In this case, the number is 6. To get it, we have to split the string by '/' followed by '?'

page_count = soup.find('div', class_= 'grid-footer-controls')
page_count_link = page_count.find_all('a') # link is inside an <a> tag
link = page_count_link[-1].get('href') # href returns the link in str
link = link.split('/')[-1] # 6 is found in the last index after splitting by '/'
max_page = int(link.split('?')[0]) # 14 is found in the first index after splitting by '?'


# In[4]:


# Function to fix the scrapped price by keeping only digits and ensuring its a float type

# Treatment for both original and display prices are the same
def price_adj(price):
    price = ''.join(filter(lambda x: x.isdigit(), price))
    price = price[:-2] + '.' + price[-2:]
    return float(price)

# Scraping all of the pages using a for loop

for page in range(1, max_page + 1): # Starts from page 1 and end at max_page + 1 due to indexing 
    source = 'https://store.playstation.com/en-sg/grid/STORE-MSF86012-SPECIALOFFER/' + str(page) + '?gameContentType=games&platform=ps4'
    source = requests.get(source).text
    soup = BeautifulSoup(source, 'lxml') 
    
    game_catalog = soup.find_all('div', class_ = 'grid-cell__body')

# There are games without a price tag. Those items would not have grid-cell__footer.
# This allows us to run a boolean if statemennt to loop through only those with a price tag
# Loop through all the games for a given page while scraping the title, original price, and discounted price

    for item in range(len(game_catalog)):
        if bool(game_catalog[item].find('div', class_ = 'grid-cell__footer')) == True:
            
            # scrap game title
            game_title = game_catalog[item].span.text
            
            # scrap original price and put it through price adj function
            game_price_original = game_catalog[item].find('span', class_ = 'grid-cell__prices-container').span.text
            game_price_original = price_adj(game_price_original)

            # scrap discounted price and put it through price adj function
            game_price_discounted = game_catalog[item].find('span', class_ = 'grid-cell__prices-container').h3.text
            game_price_discounted = price_adj(game_price_discounted)
                      
            csv_writer.writerow([game_title, game_price_original, game_price_discounted, round(1-(game_price_discounted/game_price_original), 2)])

csv_file.close()