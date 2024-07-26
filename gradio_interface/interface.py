import gradio as gr
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Quote, Author, Tag

def fetch_quotes_from_db(db: Session):
    quotes = db.query(Quote).all()
    result = []
    for quote in quotes:
        comment_lenght = min(500,len(quote.author.biography))
        quote_data = {
            "quote_text": quote.quote_text,
            "author": {
                "name": quote.author.name,
                "birth_date": quote.author.birth_date,
                "birth_place": quote.author.birth_place,
                "biography": quote.author.biography[0:comment_lenght] + '...'
            },
            "tags": [tag.name for tag in quote.tags]
        }
        result.append(quote_data)
    return result

def display_quotes():
    db = next(get_db())
    quotes = fetch_quotes_from_db(db)
    db.close()
    return quotes

def create_interface():
    def get_quotes():
        return display_quotes()
    
    iface = gr.Interface(
        fn=get_quotes,
        inputs=[],
        outputs=gr.JSON()
    )
    return iface
