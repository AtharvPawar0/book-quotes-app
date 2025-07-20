# Import necessary modules from Flask and Flask-CORS
from flask import Flask, jsonify
from flask_cors import CORS
import random

# Initialize the Flask application
app = Flask(__name__)
# Enable CORS for all routes, allowing your frontend to access this API
CORS(app)

# Define a list of quotes. You can expand this list with many more quotes!
# Each quote is a dictionary with 'quote', 'author', and 'book' keys.
quotes = [
    {
        "quote": "The only way to do great work is to love what you do.",
        "author": "Steve Jobs",
        "book": "Stanford Commencement Speech"
    },
    {
        "quote": "It is our choices, Harry, that show what we truly are, far more than our abilities.",
        "author": "J.K. Rowling",
        "book": "Harry Potter and the Chamber of Secrets"
    },
    {
        "quote": "All that is gold does not glitter, not all those who wander are lost; the old that is strong does not wither, deep roots are not frosted.",
        "author": "J.R.R. Tolkien",
        "book": "The Fellowship of the Ring"
    },
    {
        "quote": "The mind is its own place, and in itself can make a heaven of hell, a hell of heaven.",
        "author": "John Milton",
        "book": "Paradise Lost"
    },
    {
        "quote": "So many books, so little time.",
        "author": "Frank Zappa",
        "book": "Attributed"
    },
    {
        "quote": "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.",
        "author": "Ralph Waldo Emerson",
        "book": "Self-Reliance"
    },
    {
        "quote": "The future belongs to those who believe in the beauty of their dreams.",
        "author": "Eleanor Roosevelt",
        "book": "Attributed"
    },
    {
        "quote": "It was the best of times, it was the worst of times.",
        "author": "Charles Dickens",
        "book": "A Tale of Two Cities"
    },
    {
        "quote": "Do not go where the path may lead, go instead where there is no path and leave a trail.",
        "author": "Ralph Waldo Emerson",
        "book": "Attributed"
    },
    {
        "quote": "The unexamined life is not worth living.",
        "author": "Socrates",
        "book": "Apology"
    }
]

# Define the API endpoint '/api/quote'
@app.route('/api/quote', methods=['GET'])
def get_random_quote():
    """
    This function selects a random quote from the 'quotes' list
    and returns it as a JSON response.
    """
    # Use random.choice to pick one quote randomly from the list
    random_quote = random.choice(quotes)
    # Return the selected quote as a JSON object
    return jsonify(random_quote)

# This block ensures the Flask development server runs only when the script is executed directly.
# It will run on http://127.0.0.1:5000 by default.
if __name__ == '__main__':
    # For deployment, host='0.0.0.0' is often used to make it accessible externally.
    app.run(debug=True, host='0.0.0.0', port=5000)
