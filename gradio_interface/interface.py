import gradio as gr
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Quote, Author, Tag

def fetch_quotes_from_db(db: Session, author_name=None):
    if author_name:
        quotes = db.query(Quote).join(Author).filter(Author.name == author_name).all()
    else:
        quotes = db.query(Quote).all()
    
    result = []
    for quote in quotes:
        quote_data = {
            "id": quote.id,
            "author": quote.author.name, 
            "quote_text": quote.quote_text,
            "URL": quote.quote_source_url,
            "tags": [tag.name for tag in quote.tags]
        }
        result.append(quote_data)
    return result


def fetch_bio_from_db(db: Session, author_name=None):
    if author_name:

        bio_data = db.query(Author).filter(Author.name == author_name).first()
        comment_length = min(1000, len(bio_data.biography))
        result = {
            "author": {
                "name": bio_data.name,
                "birth_date": bio_data.birth_date,
                "birth_place": bio_data.birth_place,
                "biography": bio_data.biography[:comment_length] + '...'
            }
        }
        
    else:
        result = 'No se encontró la biografía'

    return result


def fetch_authors_from_db(db: Session):
    authors = db.query(Author.name).all()
    return [author[0] for author in authors]


def display_quotes(author_name=None):
    db = next(get_db())
    quotes = fetch_quotes_from_db(db, author_name)
    db.close()
    return quotes


def display_bio(author_name=None):
    db = next(get_db())
    quotes = fetch_bio_from_db(db, author_name)
    db.close()
    return quotes


def create_interface():
    with gr.Blocks() as iface:
        gr.Markdown("# JV - P4 Scrapter")
        
        with gr.Row():
            with gr.Column():
                gr.Markdown("## Frases por autor")
                author_dropdown = gr.Dropdown(label="Seleccione Autor", choices=[], interactive=True)
                quote_list = gr.JSON(label="Frases")

            with gr.Column():
                gr.Markdown("## Biografías")
                author_dropdown_2 = gr.Dropdown(label="Seleccione Autor", choices=[], interactive=True)
                bio = gr.JSON(label="Biografías")

        def update_author_dropdown():
            db = next(get_db())
            authors = fetch_authors_from_db(db)
            db.close()
            return gr.update(choices=authors)

        def get_quotes(author_name):
            return display_quotes(author_name)
        
        def get_bio(author_name):
            return display_bio(author_name)

        # Update the dropdown choices dynamically
        iface.load(fn=update_author_dropdown, inputs=None, outputs=author_dropdown)
        iface.load(fn=update_author_dropdown, inputs=None, outputs=author_dropdown_2)

        author_dropdown.change(fn=get_quotes, inputs=author_dropdown, outputs=quote_list)
        author_dropdown_2.change(fn=get_bio, inputs=author_dropdown_2, outputs=bio)

    return iface
