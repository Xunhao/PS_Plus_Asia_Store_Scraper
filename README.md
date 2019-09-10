# PS_Plus_Store_Scraper

## Goal of this project 
This project seeks to use BeautifulSoup to scrap PS Plus Store Asia for games that are currently under discount. I own a PS4 and one of my hobbies is to always be on a look out for games with good value. For example, if I feel that the content of a game that I am interested in does not worth the high price tag, I will postpone my purchase while waiting for the price to drop. As a result, I find myself constantly checking back the store for good deals. Hence, I have decided to create a script to automate this part of my hobby by simply scraping all the games that are on discount from the PS store. I hope to share this work on public for anyone that shares the same hobby as myself.

## How to use this script
IMPORTANT: Open the .py script and set your own preferred directory to store the csv file before starting the scraping process. 

PS_Plus_Scraper.py can be set to run automatically on a weekly or bi-weekly basis so that users are constantly informed of the latest deals. Sometimes, good deals are hidden and can easily be missed as they are generally listed for a short duration. As such, depending on the need of each user, one can set the frequency of execution to suit his/her own needs.

## Why not visit the site directly instead?
One of the main problems with visiting the site to check prices is that items are split into x number of pages. Each page has a maximum of 30 games on display. As such, one would need to browse through every single page to examine the catalog. If there are 180 games on discount, a user would have to wait for 6 pages to load in order to browse the entire catalog. 

With this script, all of the games are saved into a single sheeet within a csv for ease of checking. Users would also have the flexibility to sort by prices or percentage saved.

## What information have been scraped? 
1) Game title
2) Original Price
3) Discounted Price
4) Percentage Saved 

1, 2, 3 are scraped while 4 is calculate manually

## Limitations of the project
The scope of this project is limited to:
(Refer to the left panel of the website)
Device type: PS4
Content type: Games

As such, this project does not cover discounted Bundles, Add-ons, and other platforms other than PS4

## Ending note
Hope you get some of the best deals out there! :)
