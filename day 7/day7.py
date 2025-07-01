"""
🔥 PYTHON DAY 7: WEB DEVELOPMENT & DEPLOYMENT 🔥
Covers:
1. Flask Fundamentals
2. User Authentication
3. REST API Design
4. Deployment Options
"""

# ================ 1. FLASK FUNDAMENTALS ================
print("\n" + "="*60 + "\n🌐 1. FLASK WEB FRAMEWORK\n" + "="*60)

from flask import Flask, render_template_string, request

"""
🔍 Flask Basics:
- Micro web framework
- Routing: Mapping URLs to functions
- Templates: Dynamic HTML generation
"""

# 🛠️ Example 1: Minimal Flask App
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to My Flask App!</h1>"

@app.route("/hello/<name>")
def greet(name):
    return render_template_string("""
        <h1>Hello {{ name }}!</h1>
        <p>Welcome to Day 7 of Python</p>
    """, name=name)

# 🛠️ Example 2: Form Handling
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        return f"<h2>Welcome, {username}!</h2>"
    
    return """
        <form method="POST">
            <input type="text" name="username" placeholder="Enter name">
            <button type="submit">Sign Up</button>
        </form>
    """

# To run these examples:
# 1. Save this file as app.py
# 2. Run in terminal:
#    export FLASK_APP=app.py
#    flask run
# 3. Visit http://localhost:5000

# ================ 2. USER AUTHENTICATION ================
print("\n" + "="*60 + "\n🔐 2. USER AUTHENTICATION\n" + "="*60)

from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

# 🛠️ Example 3: Secure User Registration
def create_auth_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

def register_user(username, password):
    password_hash = generate_password_hash(password)
    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, password_hash) VALUES (?, ?)",
            (username, password_hash)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False  # Username exists
    finally:
        conn.close()

# 🛠️ Example 4: Login Verification
def verify_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT password_hash FROM users WHERE username = ?", 
        (username,)
    )
    result = cursor.fetchone()
    conn.close()
    
    if result and check_password_hash(result[0], password):
        return True
    return False

# Test authentication system
create_auth_db()
register_user("admin", "securepassword123")
print("Login successful?", verify_user("admin", "securepassword123"))

# ================ 3. REST API DESIGN ================
print("\n" + "="*60 + "\n🔄 3. BUILDING REST APIS\n" + "="*60)

from flask import jsonify, abort

# 🛠️ Example 5: Book API
books = [
    {"id": 1, "title": "Python Crash Course", "author": "Eric Matthes"},
    {"id": 2, "title": "Fluent Python", "author": "Luciano Ramalho"}
]

@app.route("/api/books", methods=["GET"])
def get_books():
    return jsonify(books)

@app.route("/api/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if book is None:
        abort(404)
    return jsonify(book)

# ================ 4. DEPLOYMENT OPTIONS ================
print("\n" + "="*60 + "\n🚀 4. DEPLOYING YOUR APP\n" + "="*60)

"""
🔍 Deployment Options:

1. PythonAnywhere (Beginner Friendly)
   - Free tier available
   - Web interface for management
   - Steps:
     a. Create account at pythonanywhere.com
     b. Upload your Flask app
     c. Configure WSGI file

2. Heroku (Popular Choice)
   - Free for small projects
   - CLI deployment
   - Steps:
     a. Install Heroku CLI
     b. Create Procfile: web: gunicorn app:app
     c. heroku create
     d. git push heroku main

3. AWS/GCP (Production Ready)
   - More complex setup
   - Scalable infrastructure
   - Use services like:
     - AWS Elastic Beanstalk
     - Google App Engine
"""

# ================ 🏆 5. CAPSTONE PROJECT ================
print("\n" + "="*60 + "\n🏆 5. FLASK BLOG ENGINE\n" + "="*60)

from datetime import datetime

# Configure database
def init_blog_db():
    conn = sqlite3.connect("blog.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        author TEXT NOT NULL,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()

# Blog routes
@app.route("/blog")
def blog_home():
    conn = sqlite3.connect("blog.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts ORDER BY created_at DESC")
    posts = cursor.fetchall()
    conn.close()
    
    posts_html = "\n".join(
        f"<article><h2>{p[1]}</h2><p>{p[2]}</p><small>By {p[3]}</small></article>"
        for p in posts
    )
    
    return f"""
        <h1>My Blog</h1>
        {posts_html}
        <a href="/blog/new">Create Post</a>
    """

@app.route("/blog/new", methods=["GET", "POST"])
def new_post():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        author = request.form["author"]
        
        conn = sqlite3.connect("blog.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO posts (title, content, author) VALUES (?, ?, ?)",
            (title, content, author)
        )
        conn.commit()
        conn.close()
        return "<h2>Post created!</h2><a href='/blog'>View all posts</a>"
    
    return """
        <form method="POST">
            <input type="text" name="title" placeholder="Title" required><br>
            <textarea name="content" placeholder="Content" required></textarea><br>
            <input type="text" name="author" placeholder="Your name" required><br>
            <button type="submit">Publish</button>
        </form>
    """

# Initialize and test
init_blog_db()

# ================ 📚 6. LEARNING RESOURCES ================
print("\n" + "="*60 + "\n📚 6. CONTINUE LEARNING\n" + "="*60)
print("""
1. Flask Documentation: https://flask.palletsprojects.com/
2. Deployment Guides:
   - PythonAnywhere: https://help.pythonanywhere.com/pages/Flask/
   - Heroku: https://devcenter.heroku.com/articles/getting-started-with-python
3. Advanced Topics:
   - Flask Blueprints
   - Flask-SQLAlchemy
   - Flask-Login
   - Flask RESTful
""")

if __name__ == "__main__":
    print("\n" + "="*60 + "\n🚀 RUNNING FLASK DEVELOPMENT SERVER\n" + "="*60)
    app.run(debug=True)