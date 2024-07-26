import gradio as gr
from app.database import SessionLocal
from app.models import Quote, Author, Tag

def search_quotes(query):
    db = SessionLocal()
    quotes = db.query(Quote).filter(Quote.text.ilike(f'%{query}%')).all()
    results = []
    for quote in quotes:
        author = db.query(Author).filter(Author.id == quote.author_id).first()
        tags = [tag.name for tag in quote.tags]
        results.append({
            'text': quote.text,
            'author': author.name,
            'tags': tags
        })
    return results

iface = gr.Interface(fn=search_quotes, inputs="text", outputs="json")

if __name__ == "__main__":
    iface.launch()
