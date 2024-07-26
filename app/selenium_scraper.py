from selenium import webdriver
from bs4 import BeautifulSoup
import time


#Server response waiting time
driver_waiting_time = 1
base_url = 'https://quotes.toscrape.com'


def scrape_all_quotes(driver):

    page_url = '/page/10/' #Return to 1 after PostgreSQL persisting OK
    all_quotes = []

    while page_url:
        # Navigate to one URL
        driver.get(base_url + page_url)
        # Wait for the page to load (adjust the wait time according to your webpage)
        driver.implicitly_wait(driver_waiting_time)
        # Get the HTML content of the page after it has fully loaded
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        
        #Temporary soup storage for analysis
        with open("data/soup.html", "a", encoding="utf-8") as file_soup:
            file_soup.write(str(soup))
        #

        quotes = extract_quotes(soup)
        all_quotes.extend(quotes)
        # Extract bio for each author
        for quote in quotes:
            bio = extract_author_bio(driver, quote['author_url'])
            quote.update(bio)
            time.sleep(1)  # To avoid overwhelming the server

        # Find the next page URL
        next_page = soup.find('li', class_='next')
        if next_page:
            page_url = next_page.find('a')['href']
        else:
            page_url = None

    return all_quotes


def extract_quotes(soup):

    quotes = []
    for quote in soup.find_all('div', class_='quote'):
        quote_text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
        author_url = quote.find('a')['href']
        quotes.append({'quote_text': quote_text, 'name': author, 'tags': tags, 'author_url': author_url})
    return quotes


def extract_author_bio(driver, author_url):

    driver.get(base_url + author_url)
    # Wait for the page to load (adjust the wait time according to your webpage)
    driver.implicitly_wait(driver_waiting_time)
    # Get the HTML content of the page after it has fully loaded
    html_content = driver.page_source    
    soup = BeautifulSoup(html_content, 'html.parser')  #This soup variable is only valid in this called method

    #Temporary soup storage for analysis
    with open("data/author_soup.html", "a", encoding="utf-8") as file_author_soup:
        file_author_soup.write(str(soup))
    #

    author_bio = soup.find('div', class_='author-details')
    name = author_bio.find('h3', class_='author-title').get_text().strip() 
    birth_date = author_bio.find('span', class_='author-born-date').get_text().strip()
    birth_place = author_bio.find('span', class_='author-born-location').get_text().strip()
    biography = author_bio.find('div', class_='author-description').get_text().strip()
    #author name is not returned because it is already included in the record by the quote
    return {'birth_date': birth_date, 'birth_place': birth_place[3:], 'biography': biography}

