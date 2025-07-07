from flask import Flask, render_template, request
import scraper
import sentiment
from collections import Counter

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    movie_name = request.form['movie']
    imdb_id = scraper.search_imdb_movie(movie_name)
    
    if not imdb_id:
        return "Movie not found on IMDB!"
    
    reviews = scraper.scrape_reviews(imdb_id)
    if not reviews:
        return "No reviews found for this movie."

    analyzed = sentiment.analyze_reviews(reviews)
    sentiments = [r['sentiment'] for r in analyzed]
    counts = Counter(sentiments)

    return render_template('results.html',
                           movie_name=movie_name,
                           results=analyzed,
                           counts=counts)

if __name__ == '__main__':
    app.run(debug=True)
