# Import necessary modules from Flask and Flask-CORS
from flask import Flask, jsonify
from flask_cors import CORS
import random

# Initialize the Flask application
app = Flask(__name__)
# Enable CORS for all routes, allowing your frontend to access this API
CORS(app)

# Define a list of quotes. This list has been extended with more famous book quotes!
# Each quote is a dictionary with 'quote', 'author', and 'book' keys.
quotes = [
    # General Famous Quotes (Original Set)
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
    },
    # Quotes from Requested Books (Non-Indian)
    {
        "quote": "The single most powerful asset we all have is our mind. If it is trained well, it can create enormous wealth in an instant.",
        "author": "Robert Kiyosaki",
        "book": "Rich Dad Poor Dad"
    },
    {
        "quote": "The rich buy assets. The poor and middle class buy liabilities they think are assets.",
        "author": "Robert Kiyosaki",
        "book": "Rich Dad Poor Dad"
    },
    {
        "quote": "You do not rise to the level of your goals. You fall to the level of your systems.",
        "author": "James Clear",
        "book": "Atomic Habits"
    },
    {
        "quote": "Every action you take is a vote for the type of person you wish to become.",
        "author": "James Clear",
        "book": "Atomic Habits"
    },
    {
        "quote": "The greatest power is the power of the subconscious mind. It can heal you, restore you, and make you prosperous.",
        "author": "Joseph Murphy",
        "book": "The Power of Your Subconscious Mind"
    },
    {
        "quote": "Your subconscious mind is like a rich garden, which will yield an abundance of all things, good or bad, according to the nature of the thoughts you plant in it.",
        "author": "Joseph Murphy",
        "book": "The Power of Your Subconscious Mind"
    },
    {
        "quote": "When you want something, all the universe conspires in helping you to achieve it.",
        "author": "Paulo Coelho",
        "book": "The Alchemist"
    },
    {
        "quote": "It's the possibility of having a dream come true that makes life interesting.",
        "author": "Paulo Coelho",
        "book": "The Alchemist"
    },
    {
        "quote": "Humans control the world because we are the only animals that can cooperate flexibly in large numbers.",
        "author": "Yuval Noah Harari",
        "book": "Sapiens: A Brief History of Humankind"
    },
    {
        "quote": "The confident student who thinks he is good at geometry is more likely to work hard at it and thus to do well.",
        "author": "Daniel Kahneman",
        "book": "Thinking, Fast and Slow"
    },
    {
        "quote": "War is peace. Freedom is slavery. Ignorance is strength.",
        "author": "George Orwell",
        "book": "1984"
    },
    {
        "quote": "The one thing that doesn't abide by majority rule is a person's conscience.",
        "author": "Harper Lee",
        "book": "To Kill a Mockingbird"
    },
    # General Famous Quotes (Extended Set)
    {
        "quote": "The only true wisdom is in knowing you know nothing.",
        "author": "Socrates",
        "book": "Apology"
    },
    {
        "quote": "I have not failed. I've just found 10,000 ways that won't work.",
        "author": "Thomas A. Edison",
        "book": "Attributed"
    },
    {
        "quote": "To be, or not to be: that is the question.",
        "author": "William Shakespeare",
        "book": "Hamlet"
    },
    {
        "quote": "It was a bright cold day in April, and the clocks were striking thirteen.",
        "author": "George Orwell",
        "book": "1984"
    },
    {
        "quote": "The road to hell is paved with good intentions.",
        "author": "Samuel Johnson",
        "book": "Life of Johnson"
    },
    {
        "quote": "Call me Ishmael.",
        "author": "Herman Melville",
        "book": "Moby Dick"
    },
    {
        "quote": "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.",
        "author": "Jane Austen",
        "book": "Pride and Prejudice"
    },
    {
        "quote": "There is no friend as loyal as a book.",
        "author": "Ernest Hemingway",
        "book": "Attributed"
    },
    {
        "quote": "The only thing necessary for the triumph of evil is for good men to do nothing.",
        "author": "Edmund Burke",
        "book": "Attributed"
    },
    {
        "quote": "Life is what happens to you while you're busy making other plans.",
        "author": "John Lennon",
        "book": "Beautiful Boy (Darling Boy)"
    },
    {
        "quote": "The very things that hold you down are going to lift you up.",
        "author": "Timothy Mouse",
        "book": "Dumbo"
    },
    {
        "quote": "It does not do to dwell on dreams and forget to live.",
        "author": "J.K. Rowling",
        "book": "Harry Potter and the Sorcerer's Stone"
    },
    {
        "quote": "Happiness can be found, even in the darkest of times, if one only remembers to turn on the light.",
        "author": "J.K. Rowling",
        "book": "Harry Potter and the Prisoner of Azkaban"
    },
    {
        "quote": "Never forget what you are, for surely the world will not. Make it your strength. Then it can never be your weakness.",
        "author": "George R.R. Martin",
        "book": "A Game of Thrones"
    },
    {
        "quote": "The man who does not read has no advantage over the man who cannot read.",
        "author": "Mark Twain",
        "book": "Attributed"
    },
    {
        "quote": "The greatest trick the devil ever pulled was convincing the world he didn't exist.",
        "author": "Charles Baudelaire",
        "book": "The Fanfarlo"
    },
    {
        "quote": "Do not spoil what you have by desiring what you have not; remember that what you now have was once among the things you only hoped for.",
        "author": "Epicurus",
        "book": "Vatican Sayings"
    },
    {
        "quote": "It is only with the heart that one can see rightly; what is essential is invisible to the eye.",
        "author": "Antoine de Saint-Exupéry",
        "book": "The Little Prince"
    },
    {
        "quote": "The past is a foreign country; they do things differently there.",
        "author": "L.P. Hartley",
        "book": "The Go-Between"
    },
    {
        "quote": "You can never get a cup of tea large enough or a book long enough to suit me.",
        "author": "C.S. Lewis",
        "book": "Attributed"
    },
    {
        "quote": "The world breaks everyone, and afterward, some are strong at the broken places.",
        "author": "Ernest Hemingway",
        "book": "A Farewell to Arms"
    },
    {
        "quote": "Beware; for I am fearless, and therefore powerful.",
        "author": "Mary Shelley",
        "book": "Frankenstein"
    },
    {
        "quote": "We are all in the gutter, but some of us are looking at the stars.",
        "author": "Oscar Wilde",
        "book": "Lady Windermere's Fan"
    },
    {
        "quote": "It is our light, not our darkness, that most frightens us.",
        "author": "Marianne Williamson",
        "book": "A Return to Love"
    },
    {
        "quote": "The only way out of the labyrinth of suffering is to forgive.",
        "author": "John Green",
        "book": "Looking for Alaska"
    },
    {
        "quote": "So it goes.",
        "author": "Kurt Vonnegut",
        "book": "Slaughterhouse-Five"
    },
    {
        "quote": "It's no use going back to yesterday, because I was a different person then.",
        "author": "Lewis Carroll",
        "book": "Alice's Adventures in Wonderland"
    },
    {
        "quote": "The fault, dear Brutus, is not in our stars, but in ourselves, that we are underlings.",
        "author": "William Shakespeare",
        "book": "Julius Caesar"
    },
    {
        "quote": "There is nothing to writing. All you do is sit down at a typewriter and bleed.",
        "author": "Ernest Hemingway",
        "book": "Attributed"
    },
    {
        "quote": "You have brains in your head. You have feet in your shoes. You can steer yourself any direction you choose.",
        "author": "Dr. Seuss",
        "book": "Oh, the Places You'll Go!"
    },
    {
        "quote": "It is not the strongest of the species that survives, nor the most intelligent that survives. It is the one that is most adaptable to change.",
        "author": "Charles Darwin",
        "book": "Attributed (often misattributed, but captures his essence)"
    },
    {
        "quote": "Imagination is more important than knowledge.",
        "author": "Albert Einstein",
        "book": "Attributed"
    },
    {
        "quote": "The future belongs to those who believe in the beauty of their dreams.",
        "author": "Eleanor Roosevelt",
        "book": "Attributed"
    },
    # Indian Famous Book Quotes - Bhagavad Gita (Max 10 quotes)
    {
        "quote": "Perform your duty, but do not be attached to the fruits of your actions.",
        "author": "Lord Krishna",
        "book": "Bhagavad Gita"
    },
    {
        "quote": "The mind is restless, turbulent, obstinate and very strong, O Krishna, and to subdue it is more difficult than controlling the wind.",
        "author": "Arjuna",
        "book": "Bhagavad Gita"
    },
    {
        "quote": "Whatever happened, happened for the good. Whatever is happening, is happening for the good. Whatever will happen, will also happen for the good.",
        "author": "Lord Krishna",
        "book": "Bhagavad Gita"
    },
    {
        "quote": "Lust, anger, and greed are the three gates to hell.",
        "author": "Lord Krishna",
        "book": "Bhagavad Gita"
    },
    {
        "quote": "It is better to live your own destiny imperfectly than to live an imitation of somebody else's life perfectly.",
        "author": "Bhagavad Gita",
        "book": "Bhagavad Gita"
    },
    {
        "quote": "Man is a creature of his beliefs. As he believes, so he is.",
        "author": "Bhagavad Gita",
        "book": "Bhagavad Gita"
    },
    {
        "quote": "The soul is neither born, nor does it die. It is unborn, eternal, ever-existing and primeval. It is not slain when the body is slain.",
        "author": "Bhagavad Gita",
        "book": "Bhagavad Gita"
    },
    {
        "quote": "Set thy heart upon thy work, but never on its reward.",
        "author": "Bhagavad Gita",
        "book": "Bhagavad Gita"
    },
    {
        "quote": "The disciplined mind is a person's best friend, but an undisciplined mind is a person's greatest enemy.",
        "author": "Bhagavad Gita",
        "book": "Bhagavad Gita"
    },
    {
        "quote": "The wise regulate their senses and mind, and fix their consciousness upon Me.",
        "author": "Bhagavad Gita",
        "book": "Bhagavad Gita"
    },
    # Indian Famous Book Quotes - Chanakya Niti (Max 10 quotes)
    {
        "quote": "Education is the best friend. An educated person is respected everywhere. Education beats the beauty and the youth.",
        "author": "Chanakya",
        "book": "Chanakya Niti"
    },
    {
        "quote": "A man is great by his deeds, not by birth.",
        "author": "Chanakya",
        "book": "Chanakya Niti"
    },
    {
        "quote": "As soon as the fear approaches near, attack and destroy it.",
        "author": "Chanakya",
        "book": "Chanakya Niti"
    },
    {
        "quote": "The fragrance of flowers spreads only in the direction of the wind. But the goodness of a person spreads in all directions.",
        "author": "Chanakya",
        "book": "Chanakya Niti"
    },
    {
        "quote": "Never make friends with people who are above or below you in status. Such friendships will never give you any happiness.",
        "author": "Chanakya",
        "book": "Chanakya Niti"
    },
    {
        "quote": "A truly wise man is he who knows what to say, when to say it, and to whom.",
        "author": "Chanakya",
        "book": "Chanakya Niti"
    },
    {
        "quote": "Do not reveal your secrets to anyone. It will destroy you.",
        "author": "Chanakya",
        "book": "Chanakya Niti"
    },
    {
        "quote": "The biggest guru-mantra is: never share your secrets with anybody. It will destroy you.",
        "author": "Chanakya",
        "book": "Chanakya Niti"
    },
    {
        "quote": "He who is overly attached to his family members experiences fear and sorrow, for the root of sorrow is attachment. Thus one must give up attachment to be happy.",
        "author": "Chanakya",
        "book": "Chanakya Niti"
    },
    {
        "quote": "The world's biggest power is the youth and beauty of a woman.",
        "author": "Chanakya",
        "book": "Chanakya Niti"
    },
    # Indian Famous Book Quotes - Gitanjali by Rabindranath Tagore (Max 10 quotes)
    {
        "quote": "Where the mind is without fear and the head is held high; Where knowledge is free.",
        "author": "Rabindranath Tagore",
        "book": "Gitanjali"
    },
    {
        "quote": "The highest education is that which does not merely give us information but makes our life in harmony with all existence.",
        "author": "Rabindranath Tagore",
        "book": "Sadhana: The Realisation of Life"
    },
    {
        "quote": "Clouds come floating into my life, no longer to carry rain or usher storm, but to add color to my sunset sky.",
        "author": "Rabindranath Tagore",
        "book": "Stray Birds"
    },
    {
        "quote": "Let your life lightly dance on the edges of time like dew on the tip of a leaf.",
        "author": "Rabindranath Tagore",
        "book": "Stray Birds"
    },
    {
        "quote": "We read the world wrong and say that it deceives us.",
        "author": "Rabindranath Tagore",
        "book": "Stray Birds"
    },
    {
        "quote": "The small wisdom is like water in a glass: clear, transparent, pure. The great wisdom is like the water in the sea: dark, mysterious, unfathomable.",
        "author": "Rabindranath Tagore",
        "book": "Stray Birds"
    },
    {
        "quote": "Every child comes with the message that God is not yet discouraged of man.",
        "author": "Rabindranath Tagore",
        "book": "Stray Birds"
    },
    {
        "quote": "Faith is the bird that feels the light and sings when the dawn is still dark.",
        "author": "Rabindranath Tagore",
        "book": "Stray Birds"
    },
    {
        "quote": "Love is the only reality and it is not a mere sentiment. It is the ultimate truth that lies at the heart of creation.",
        "author": "Rabindranath Tagore",
        "book": "Sadhana: The Realisation of Life"
    },
    {
        "quote": "I slept and dreamt that life was joy. I awoke and saw that life was service. I acted and behold, service was joy.",
        "author": "Rabindranath Tagore",
        "book": "Attributed"
    },
    # Indian Famous Book Quotes - Jiddu Krishnamurti (Max 10 quotes)
    {
        "quote": "There is no end to education. It is not that you read a book, pass an examination, and finish with education. The whole of life, from the moment you are born to the moment you die, is a process of learning.",
        "author": "Jiddu Krishnamurti",
        "book": "Freedom from the Known"
    },
    {
        "quote": "It is no measure of health to be well adjusted to a profoundly sick society.",
        "author": "Jiddu Krishnamurti",
        "book": "Attributed"
    },
    {
        "quote": "The highest form of human intelligence is to observe yourself without judgment.",
        "author": "Jiddu Krishnamurti",
        "book": "Attributed"
    },
    {
        "quote": "Truth is a pathless land.",
        "author": "Jiddu Krishnamurti",
        "book": "The First and Last Freedom"
    },
    {
        "quote": "The moment you have in your heart this extraordinary thing called love and feel the depth, the delight, the ecstasy of it, you will discover that for you the world is transformed.",
        "author": "Jiddu Krishnamurti",
        "book": "Freedom from the Known"
    },
    {
        "quote": "Freedom is not a reaction; freedom is not a choice. It is man's abode. It is not where he goes, but where he is.",
        "author": "Jiddu Krishnamurti",
        "book": "Freedom from the Known"
    },
    {
        "quote": "The ending of sorrow is the beginning of wisdom.",
        "author": "Jiddu Krishnamurti",
        "book": "The First and Last Freedom"
    },
    {
        "quote": "You are the world, and the world is you.",
        "author": "Jiddu Krishnamurti",
        "book": "Attributed"
    },
    {
        "quote": "To understand is to transform what is.",
        "author": "Jiddu Krishnamurti",
        "book": "Freedom from the Known"
    },
    {
        "quote": "Fear is not an abstraction; it is a living entity, an energy that you have created.",
        "author": "Jiddu Krishnamurti",
        "book": "The Awakening of Intelligence"
    },
    # Indian Famous Book Quotes - The Monk Who Sold His Ferrari by Robin Sharma (Max 10 quotes)
    {
        "quote": "The mind is a wonderful servant, but a terrible master.",
        "author": "Robin Sharma",
        "book": "The Monk Who Sold His Ferrari"
    },
    {
        "quote": "Small daily improvements are the key to staggering long-term results.",
        "author": "Robin Sharma",
        "book": "The Monk Who Sold His Ferrari"
    },
    {
        "quote": "To be a great leader, you must first become a great human being.",
        "author": "Robin Sharma",
        "book": "The Monk Who Sold His Ferrari"
    },
    {
        "quote": "Invest in yourself. It's the only investment that will give you unlimited returns.",
        "author": "Robin Sharma",
        "book": "The Monk Who Sold His Ferrari"
    },
    {
        "quote": "The purpose of life is a life of purpose.",
        "author": "Robin Sharma",
        "book": "The Monk Who Sold His Ferrari"
    },
    {
        "quote": "What the mind can conceive and believe, it can achieve.",
        "author": "Robin Sharma",
        "book": "The Monk Who Sold His Ferrari"
    },
    {
        "quote": "The best way to predict the future is to create it.",
        "author": "Robin Sharma",
        "book": "The Monk Who Sold His Ferrari"
    },
    {
        "quote": "Don't live the same year 75 times and call it a life.",
        "author": "Robin Sharma",
        "book": "The Monk Who Sold His Ferrari"
    },
    {
        "quote": "The more you learn, the more you earn.",
        "author": "Robin Sharma",
        "book": "The Monk Who Sold His Ferrari"
    },
    {
        "quote": "The journey of a thousand miles begins with a single step.",
        "author": "Robin Sharma",
        "book": "The Monk Who Sold His Ferrari"
    },
    # Indian Famous Book Quotes - The Palace of Illusions by Chitra Banerjee Divakaruni (Max 10 quotes)
    {
        "quote": "A woman's life is a series of compromises.",
        "author": "Chitra Banerjee Divakaruni",
        "book": "The Palace of Illusions"
    },
    {
        "quote": "There are some things that cannot be changed, no matter how much we wish they could.",
        "author": "Chitra Banerjee Divakaruni",
        "book": "The Palace of Illusions"
    },
    {
        "quote": "Memory, like a house, has many rooms.",
        "author": "Chitra Banerjee Divakaruni",
        "book": "The Palace of Illusions"
    },
    {
        "quote": "The past is a foreign country; they do things differently there.",
        "author": "Chitra Banerjee Divakaruni",
        "book": "The Palace of Illusions"
    },
    {
        "quote": "Love is a dangerous thing. It can make you do things you never thought possible.",
        "author": "Chitra Banerjee Divakaruni",
        "book": "The Palace of Illusions"
    },
    {
        "quote": "Sometimes, the only way to find yourself is to lose yourself completely.",
        "author": "Chitra Banerjee Divakaruni",
        "book": "The Palace of Illusions"
    },
    {
        "quote": "Every choice we make creates a new path.",
        "author": "Chitra Banerjee Divakaruni",
        "book": "The Palace of Illusions"
    },
    {
        "quote": "The greatest battles are fought within ourselves.",
        "author": "Chitra Banerjee Divakaruni",
        "book": "The Palace of Illusions"
    },
    {
        "quote": "Silence can be more powerful than words.",
        "author": "Chitra Banerjee Divakaruni",
        "book": "The Palace of Illusions"
    },
    {
        "quote": "Destiny is not a matter of chance; it is a matter of choice.",
        "author": "Chitra Banerjee Divakaruni",
        "book": "The Palace of Illusions"
    },
    # Indian Famous Book Quotes - The God of Small Things by Arundhati Roy (Max 10 quotes)
    {
        "quote": "It was a time when the world was changing, and so were they.",
        "author": "Arundhati Roy",
        "book": "The God of Small Things"
    },
    {
        "quote": "The secret of the Big Stories is that they have no secrets. They are plain and simple.",
        "author": "Arundhati Roy",
        "book": "The God of Small Things"
    },
    {
        "quote": "Things can change in a day. A single day. But sometimes, a single day can change everything.",
        "author": "Arundhati Roy",
        "book": "The God of Small Things"
    },
    {
        "quote": "To understand history, you have to understand the stories.",
        "author": "Arundhati Roy",
        "book": "The God of Small Things"
    },
    {
        "quote": "The only way to grieve is to remember.",
        "author": "Arundhati Roy",
        "book": "The God of Small Things"
    },
    {
        "quote": "Certain things, once experienced, can never be forgotten.",
        "author": "Arundhati Roy",
        "book": "The God of Small Things"
    },
    {
        "quote": "The heart has its reasons, which reason knows nothing of.",
        "author": "Arundhati Roy",
        "book": "The God of Small Things"
    },
    {
        "quote": "Small things are always the most important.",
        "author": "Arundhati Roy",
        "book": "The God of Small Things"
    },
    {
        "quote": "The past was a country, and they were its refugees.",
        "author": "Arundhati Roy",
        "book": "The God of Small Things"
    },
    {
        "quote": "Love is a dangerous thing. It can make you do things you never thought possible.",
        "author": "Arundhati Roy",
        "book": "The God of Small Things"
    },
    # Indian Famous Book Quotes - A Suitable Boy by Vikram Seth (Max 10 quotes)
    {
        "quote": "You can't live your life for other people. You've got to do what's right for you, even if it hurts someone you love.",
        "author": "Vikram Seth",
        "book": "A Suitable Boy"
    },
    {
        "quote": "The world is full of people who are trying to tell you what to do. Don't listen to them.",
        "author": "Vikram Seth",
        "book": "A Suitable Boy"
    },
    {
        "quote": "Life is a series of choices. Every choice you make shapes your future.",
        "author": "Vikram Seth",
        "book": "A Suitable Boy"
    },
    {
        "quote": "It is not enough to be good; you must be good for something.",
        "author": "Vikram Seth",
        "book": "A Suitable Boy"
    },
    {
        "quote": "The past is never dead. It's not even past.",
        "author": "Vikram Seth",
        "book": "A Suitable Boy"
    },
    {
        "quote": "To love is to suffer. To avoid suffering, one must not love. But then one suffers from not loving.",
        "author": "Vikram Seth",
        "book": "A Suitable Boy"
    },
    {
        "quote": "The most important thing in life is to be true to yourself.",
        "author": "Vikram Seth",
        "book": "A Suitable Boy"
    },
    {
        "quote": "There is no such thing as a perfect life. There are only perfect moments.",
        "author": "Vikram Seth",
        "book": "A Suitable Boy"
    },
    {
        "quote": "The greatest joy in life is to love and be loved.",
        "author": "Vikram Seth",
        "book": "A Suitable Boy"
    },
    {
        "quote": "Change is the only constant in life.",
        "author": "Vikram Seth",
        "book": "A Suitable Boy"
    },
    # Indian Famous Book Quotes - The White Tiger by Aravind Adiga (Max 10 quotes)
    {
        "quote": "The only way to get out of the Rooster Coop is to kill the Rooster.",
        "author": "Aravind Adiga",
        "book": "The White Tiger"
    },
    {
        "quote": "In India, you don't rise from your caste. You are given a caste at birth and that is your destiny.",
        "author": "Aravind Adiga",
        "book": "The White Tiger"
    },
    {
        "quote": "The future of the world is in the East, not the West.",
        "author": "Aravind Adiga",
        "book": "The White Tiger"
    },
    {
        "quote": "The greatest thing about this country is that you can be anything you want to be, if you're willing to work for it.",
        "author": "Aravind Adiga",
        "book": "The White Tiger"
    },
    {
        "quote": "The poor in India are like chickens in a coop. They are born, they live, they die, and they never leave the coop.",
        "author": "Aravind Adiga",
        "book": "The White Tiger"
    },
    {
        "quote": "The true measure of a man is how he treats those who are beneath him.",
        "author": "Aravind Adiga",
        "book": "The White Tiger"
    },
    {
        "quote": "The rich are like gods in India. They can do whatever they want, and no one can stop them.",
        "author": "Aravind Adiga",
        "book": "The White Tiger"
    },
    {
        "quote": "The only way to get ahead in India is to be ruthless.",
        "author": "Aravind Adiga",
        "book": "The White Tiger"
    },
    {
        "quote": "Corruption is the oil that lubricates the wheels of India.",
        "author": "Aravind Adiga",
        "book": "The White Tiger"
    },
    {
        "quote": "The world is a jungle, and only the strong survive.",
        "author": "Aravind Adiga",
        "book": "The White Tiger"
    },
    # Indian Famous Book Quotes - Midnight's Children by Salman Rushdie (Max 10 quotes)
    {
        "quote": "To understand me, you have to swallow a world.",
        "author": "Salman Rushdie",
        "book": "Midnight's Children"
    },
    {
        "quote": "Who what am I? My answer: I am the sum of everything that has happened to me.",
        "author": "Salman Rushdie",
        "book": "Midnight's Children"
    },
    {
        "quote": "Memory, like a house, has many rooms.",
        "author": "Salman Rushdie",
        "book": "Midnight's Children"
    },
    {
        "quote": "Children are the future, but they are also the past.",
        "author": "Salman Rushdie",
        "book": "Midnight's Children"
    },
    {
        "quote": "The past is never dead. It's not even past.",
        "author": "Salman Rushdie",
        "book": "Midnight's Children"
    },
    {
        "quote": "History is a nightmare from which I am trying to awake.",
        "author": "Salman Rushdie",
        "book": "Midnight's Children"
    },
    {
        "quote": "The truth is a dangerous thing.",
        "author": "Salman Rushdie",
        "book": "Midnight's Children"
    },
    {
        "quote": "To be born again, you must first die.",
        "author": "Salman Rushdie",
        "book": "Midnight's Children"
    },
    {
        "quote": "The world is a stage, and all the men and women merely players.",
        "author": "Salman Rushdie",
        "book": "Midnight's Children"
    },
    {
        "quote": "Life is a story. Make it a good one.",
        "author": "Salman Rushdie",
        "book": "Midnight's Children"
    },
    # Indian Famous Book Quotes - Ignited Minds by A.P.J. Abdul Kalam (Max 10 quotes)
    {
        "quote": "Dreams are not those which you see in sleep, but those that do not let you sleep.",
        "author": "A.P.J. Abdul Kalam",
        "book": "Ignited Minds"
    },
    {
        "quote": "Excellence is a continuous process and not an accident.",
        "author": "A.P.J. Abdul Kalam",
        "book": "Ignited Minds"
    },
    {
        "quote": "To succeed in your mission, you must have single-minded devotion to your goal.",
        "author": "A.P.J. Abdul Kalam",
        "book": "Ignited Minds"
    },
    {
        "quote": "Educationists should build the capacities of the spirit of inquiry, creativity, entrepreneurial and moral leadership among students and become their role model.",
        "author": "A.P.J. Abdul Kalam",
        "book": "Ignited Minds"
    },
    {
        "quote": "My 2020 Vision for India is to transform India into a developed nation.",
        "author": "A.P.J. Abdul Kalam",
        "book": "Ignited Minds"
    },
    {
        "quote": "Thinking is the capital, Enterprise is the way, Hard Work is the solution.",
        "author": "A.P.J. Abdul Kalam",
        "book": "Ignited Minds"
    },
    {
        "quote": "If a country is to be corruption free and become a nation of beautiful minds, I strongly feel there are three key societal members who can make a difference. They are the father, the mother and the teacher.",
        "author": "A.P.J. Abdul Kalam",
        "book": "Ignited Minds"
    },
    {
        "quote": "Let us sacrifice our today so that our children can have a better tomorrow.",
        "author": "A.P.J. Abdul Kalam",
        "book": "Ignited Minds"
    },
    {
        "quote": "The youth need to be enabled to become job generators from job seekers.",
        "author": "A.P.J. Abdul Kalam",
        "book": "Ignited Minds"
    },
    {
        "quote": "We are all born with a divine fire in us. Our efforts should be to give wings to this fire.",
        "author": "A.P.J. Abdul Kalam",
        "book": "Ignited Minds"
    },
    # Indian Famous Book Quotes - Wings of Fire by A.P.J. Abdul Kalam (Max 10 quotes)
    {
        "quote": "We are all born with a divine fire in us. Our efforts should be to give wings to this fire.",
        "author": "A.P.J. Abdul Kalam",
        "book": "Wings of Fire"
    },
    {
        "quote": "If you want to shine like a sun, first burn like a sun.",
        "author": "A.P.J. Abdul Kalam",
        "book": "Wings of Fire"
    },
    {
        "quote": "Confidence and hard work is the best medicine to kill the disease called failure. It will make you a successful person.",
        "author": "A.P.J. Abdul Kalam",
        "book": "Wings of Fire"
    },
    {
        "quote": "Look at the sky. We are not alone. The whole universe is friendly to us and conspires to give the best to those who dream and work.",
        "author": "A.P.J. Abdul Kalam",
        "book": "Wings of Fire"
    },
    {
        "quote": "Man needs difficulties in life because they are necessary to enjoy the success.",
        "author": "A.P.J. Abdul Kalam",
        "book": "Wings of Fire"
    },
    {
        "quote": "To succeed in your mission, you must have single-minded devotion to your goal.",
        "author": "A.P.J. Abdul Kalam",
        "book": "Wings of Fire"
    },
    {
        "quote": "Learning gives creativity, Creativity leads to thinking, Thinking provides knowledge, Knowledge makes you great.",
        "author": "A.P.J. Abdul Kalam",
        "book": "Wings of Fire"
    },
    {
        "quote": "Don't take rest after your first victory because if you fail in second, more lips are waiting to say that your first victory was just luck.",
        "author": "A.P.J. Abdul Kalam",
        "book": "Wings of Fire"
    },
    {
        "quote": "You have to dream before your dreams can come true.",
        "author": "A.P.J. Abdul Kalam",
        "book": "Wings of Fire"
    },
    {
        "quote": "Failure will never overtake me if my determination to succeed is strong enough.",
        "author": "A.P.J. Abdul Kalam",
        "book": "Wings of Fire"
    },
    # Indian Famous Book Quotes - The Guide by R.K. Narayan (Max 10 quotes)
    {
        "quote": "If you are too careful, you are sure to miss out on life.",
        "author": "R.K. Narayan",
        "book": "The Guide"
    },
    {
        "quote": "The world is full of strange people, and stranger things happen in it.",
        "author": "R.K. Narayan",
        "book": "The Guide"
    },
    {
        "quote": "One must be content with what one has, and not fret about what one does not have.",
        "author": "R.K. Narayan",
        "book": "The Guide"
    },
    {
        "quote": "A man's life is a journey, and he must walk it alone.",
        "author": "R.K. Narayan",
        "book": "The Guide"
    },
    {
        "quote": "The greatest truth is that there is no truth.",
        "author": "R.K. Narayan",
        "book": "The Guide"
    },
    {
        "quote": "Life is a comedy to those who think, a tragedy to those who feel.",
        "author": "R.K. Narayan",
        "book": "The Guide"
    },
    {
        "quote": "The only way to find happiness is to give it to others.",
        "author": "R.K. Narayan",
        "book": "The Guide"
    },
    {
        "quote": "The world is a stage, and all the men and women merely players.",
        "author": "R.K. Narayan",
        "book": "The Guide"
    },
    {
        "quote": "The past is a foreign country; they do things differently there.",
        "author": "R.K. Narayan",
        "book": "The Guide"
    },
    {
        "quote": "Every moment is a fresh beginning.",
        "author": "R.K. Narayan",
        "book": "The Guide"
    },
    # Indian Famous Book Quotes - Train to Pakistan by Khushwant Singh (Max 10 quotes)
    {
        "quote": "Religion is not a matter of God or the devil. It is a matter of man.",
        "author": "Khushwant Singh",
        "book": "Train to Pakistan"
    },
    {
        "quote": "The only way to survive is to be ruthless.",
        "author": "Khushwant Singh",
        "book": "Train to Pakistan"
    },
    {
        "quote": "Hate is a dangerous thing. It can consume you.",
        "author": "Khushwant Singh",
        "book": "Train to Pakistan"
    },
    {
        "quote": "The partition of India was a tragedy. It divided a nation and tore families apart.",
        "author": "Khushwant Singh",
        "book": "Train to Pakistan"
    },
    {
        "quote": "There is no such thing as good and evil. There is only survival.",
        "author": "Khushwant Singh",
        "book": "Train to Pakistan"
    },
    {
        "quote": "The greatest crime is to be silent in the face of injustice.",
        "author": "Khushwant Singh",
        "book": "Train to Pakistan"
    },
    {
        "quote": "The world is a cruel place, and only the strong survive.",
        "author": "Khushwant Singh",
        "book": "Train to Pakistan"
    },
    {
        "quote": "To forgive is to be free.",
        "author": "Khushwant Singh",
        "book": "Train to Pakistan"
    },
    {
        "quote": "The past is a burden. The future is a mystery. The present is a gift.",
        "author": "Khushwant Singh",
        "book": "Train to Pakistan"
    },
    {
        "quote": "Life is a journey, and we must all walk it alone.",
        "author": "Khushwant Singh",
        "book": "Train to Pakistan"
    },
    # Indian Famous Book Quotes - Discovery of India by Jawaharlal Nehru (Max 10 quotes)
    {
        "quote": "Culture is the widening of the mind and of the spirit.",
        "author": "Jawaharlal Nehru",
        "book": "The Discovery of India"
    },
    {
        "quote": "The only way to live is to learn, to grow, to evolve.",
        "author": "Jawaharlal Nehru",
        "book": "The Discovery of India"
    },
    {
        "quote": "Peace is not merely the absence of war, but the presence of justice, of law, of order - in short, of government.",
        "author": "Jawaharlal Nehru",
        "book": "The Discovery of India"
    },
    {
        "quote": "The greatest danger in life is to take too many precautions.",
        "author": "Jawaharlal Nehru",
        "book": "The Discovery of India"
    },
    {
        "quote": "A moment of truth comes rarely, and when it does, it is often painful.",
        "author": "Jawaharlal Nehru",
        "book": "The Discovery of India"
    },
    {
        "quote": "The essential characteristic of a truly cultured person is the absence of arrogance.",
        "author": "Jawaharlal Nehru",
        "book": "The Discovery of India"
    },
    {
        "quote": "Democracy is good. I say this because other systems are worse.",
        "author": "Jawaharlal Nehru",
        "book": "The Discovery of India"
    },
    {
        "quote": "Facts are facts and will not disappear on account of your likes.",
        "author": "Jawaharlal Nehru",
        "book": "The Discovery of India"
    },
    {
        "quote": "The only way to deal with an unfree world is to become so absolutely free that your very existence is an act of rebellion.",
        "author": "Jawaharlal Nehru",
        "book": "The Discovery of India"
    },
    {
        "quote": "Life is like a game of cards. The hand that is dealt you is determinism; the way you play it is free will.",
        "author": "Jawaharlal Nehru",
        "book": "The Discovery of India"
    },
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
