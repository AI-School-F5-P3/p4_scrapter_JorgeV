from selenium import webdriver
from app.selenium_scraper import scrape_all_quotes

from app.database import engine, Base, get_db
from app.models import Quote, Author, Tag

def persist_data(db, quotes):
    for quote in quotes:
        print (quote)
        author = db.query(Author).filter(Author.name == quote['name']).first()
        if not author:
            author = Author(
                name=quote['name'],
                birth_date=quote['birth_date'],
                birth_place=quote['birth_place'],
                biography=quote['biography']
            )
            db.add(author)
            db.commit()
            db.refresh(author)

        quote_record = db.query(Quote).filter(Quote.quote_text == quote['quote_text']).first()
        if not quote_record:
            quote_record = Quote(quote_text=quote['quote_text'], author_id=author.id)
            db.add(quote_record)
            db.commit()
            db.refresh(quote_record)

        for tag_name in quote['tags']:
            tag = db.query(Tag).filter(Tag.name == tag_name).first()
            if not tag:
                tag = Tag(name=tag_name)
                db.add(tag)
                db.commit()
                db.refresh(tag)
            
            if tag not in quote_record.tags:
                quote_record.tags.append(tag)
                
        db.commit()


if __name__ == '__main__':

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        Base.metadata.create_all(bind=engine)
        # Scrape all quotes
        
        quotes_data = scrape_all_quotes(driver)

        #Saving all quote data for reference
        with open("data/quotes.txt", "w", encoding="utf-8") as file:
            file.write(str(quotes_data))

        # Use get_db function to manage the database session
        db_gen = get_db()
        db = next(db_gen)
        try:
            persist_data(db, quotes_data)
        finally:
            db.close()


        # Temporary Print the extracted quotes
        for quote in quotes_data:
            print(quote['quote_text'])

    finally:
        driver.quit()