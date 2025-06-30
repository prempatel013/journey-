"""
🐍 PYTHON DAY 6 MASTER FILE: DATABASES & DATA ANALYSIS 🐍
Covers:
1. SQLite Fundamentals
2. SQLAlchemy ORM
3. Pandas Data Analysis
4. Real-World Projects
"""

# ================ 1. SQLITE FUNDAMENTALS ================
print("\n" + "="*60 + "\n💾 1. SQLITE DATABASES\n" + "="*60)

import sqlite3
from contextlib import closing

"""
🔍 SQLite Basics:
- Serverless database (single file)
- Supports standard SQL
- Ideal for local apps and prototyping
"""

# 🛠️ Example 1: Creating a Database
def create_database():
    with closing(sqlite3.connect("library.db")) as conn:
        cursor = conn.cursor()
        
        # Create tables
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT,
            year INTEGER
        )
        """)
        
        # Insert sample data
        books = [
            ("The Hobbit", "J.R.R. Tolkien", 1937),
            ("1984", "George Orwell", 1949),
            ("Python Crash Course", "Eric Matthes", 2015)
        ]
        cursor.executemany("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", books)
        conn.commit()
    print("✅ Database created with sample books!")

create_database()

# 🛠️ Example 2: Querying Data
def query_books():
    with closing(sqlite3.connect("library.db")) as conn:
        conn.row_factory = sqlite3.Row  # Access columns by name
        cursor = conn.cursor()
        
        print("\nAll Books:")
        cursor.execute("SELECT * FROM books")
        for row in cursor.fetchall():
            print(f"{row['id']}. {row['title']} ({row['year']})")
        
        print("\nBooks after 1950:")
        cursor.execute("SELECT title FROM books WHERE year > ?", (1950,))
        print([row[0] for row in cursor.fetchall()])

query_books()

# ================ 2. SQLALCHEMY ORM ================
print("\n" + "="*60 + "\n🔮 2. SQLALCHEMY ORM\n" + "="*60)

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# 🛠️ Example 3: Defining Models
class Book(Base):
    __tablename__ = 'books_orm'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    author = Column(String(50))
    year = Column(Integer)

# Initialize database
engine = create_engine('sqlite:///library_orm.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# 🛠️ Example 4: ORM Operations
def orm_demo():
    session = Session()
    
    # Add new books
    new_books = [
        Book(title="Clean Code", author="Robert Martin", year=2008),
        Book(title="Design Patterns", author="Gang of Four", year=1994)
    ]
    session.add_all(new_books)
    session.commit()
    
    # Query data
    print("\nORM Query Results:")
    recent_books = session.query(Book).filter(Book.year > 2000).all()
    for book in recent_books:
        print(f"{book.id}. {book.title} ({book.year})")
    
    session.close()

orm_demo()

# ================ 3. PANDAS DATA ANALYSIS ================
print("\n" + "="*60 + "\n📊 3. PANDAS DATA ANALYSIS\n" + "="*60)

import pandas as pd
import numpy as np

# 🛠️ Example 5: Basic DataFrame Operations
def pandas_basics():
    # Create DataFrame from SQL
    with closing(sqlite3.connect("library.db")) as conn:
        df = pd.read_sql("SELECT * FROM books", conn)
    
    print("\nLibrary DataFrame:")
    print(df.head())
    
    # Data analysis
    print("\nBasic Stats:")
    print(f"Total books: {len(df)}")
    print(f"Oldest book: {df['year'].min()}")
    print(f"Authors: {df['author'].unique().tolist()}")
    
    # Add new column
    df['century'] = np.where(df['year'] < 2000, '20th', '21st')
    print("\nBooks by Century:")
    print(df[['title', 'century']])

pandas_basics()

# 🛠️ Example 6: Advanced Analysis
def pandas_analysis():
    # Create sample sales data
    sales_data = {
        'book_id': [1, 2, 3, 1, 2],
        'sale_date': ['2023-01-15', '2023-01-15', '2023-01-16', '2023-01-17', '2023-01-18'],
        'price': [12.99, 9.99, 24.99, 12.99, 9.99]
    }
    sales = pd.DataFrame(sales_data)
    sales['sale_date'] = pd.to_datetime(sales['sale_date'])
    
    # Merge with book data
    with closing(sqlite3.connect("library.db")) as conn:
        books = pd.read_sql("SELECT id, title FROM books", conn)
    
    merged = pd.merge(sales, books, left_on='book_id', right_on='id')
    
    print("\nSales Analysis:")
    print(f"Total revenue: ${merged['price'].sum():.2f}")
    print("\nTop Selling Books:")
    print(merged.groupby('title')['price'].sum().sort_values(ascending=False))

pandas_analysis()

# ================ 🏆 4. REAL-WORLD PROJECTS ================
print("\n" + "="*60 + "\n🏆 4. REAL-WORLD PROJECTS\n" + "="*60)

# 🔧 Project 1: Personal Finance Tracker
class FinanceTracker:
    def __init__(self):
        self.engine = create_engine('sqlite:///finance.db')
        self._setup_database()
    
    def _setup_database(self):
        with self.engine.connect() as conn:
            conn.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                description TEXT,
                amount REAL,
                category TEXT
            )
            """)
    
    def add_transaction(self, date, description, amount, category):
        with self.engine.connect() as conn:
            conn.execute(
                "INSERT INTO transactions (date, description, amount, category) VALUES (?, ?, ?, ?)",
                (date, description, amount, category)
            )
        print("✅ Transaction added!")
    
    def generate_report(self):
        with self.engine.connect() as conn:
            df = pd.read_sql("SELECT * FROM transactions", conn)
        
        if df.empty:
            print("No transactions found")
            return
        
        print("\n💵 Financial Report:")
        print(f"Total Transactions: {len(df)}")
        print(f"Net Balance: ${df['amount'].sum():.2f}")
        
        print("\n📊 By Category:")
        print(df.groupby('category')['amount'].sum().sort_values())

# Usage
tracker = FinanceTracker()
tracker.add_transaction("2023-06-01", "Grocery Shopping", -85.50, "Food")
tracker.add_transaction("2023-06-02", "Paycheck", 2500.00, "Income")
tracker.generate_report()

# 🔧 Project 2: Bookstore Inventory System
class BookstoreInventory:
    def __init__(self):
        self.engine = create_engine('sqlite:///bookstore.db')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
    
    def add_book(self, title, author, price, quantity):
        session = self.Session()
        book = Book(title=title, author=author, price=price, quantity=quantity)
        session.add(book)
        session.commit()
        session.close()
        print(f"📚 Added {title} to inventory")
    
    def check_stock(self):
        session = self.Session()
        low_stock = session.query(Book).filter(Book.quantity < 5).all()
        
        if low_stock:
            print("\n⚠️ Low Stock Alert:")
            for book in low_stock:
                print(f"{book.title} - Only {book.quantity} left")
        else:
            print("\nAll items sufficiently stocked")
        
        session.close()

# ================ 🚀 5. NEXT STEPS ================
print("\n" + "="*60 + "\n🚀 5. WHERE TO GO NEXT\n" + "="*60)
print("""
1. Advanced Databases:
   - PostgreSQL/MySQL integration
   - Database migrations (Alembic)
   - Redis for caching

2. Data Science:
   - Pandas advanced features (time series)
   - Visualization with Matplotlib/Seaborn
   - Machine learning integration

3. Web Development:
   - FastAPI/SQLAlchemy backends
   - Django ORM
   - Database-as-a-service (Firebase, Supabase)

4. Production Skills:
   - Containerization (Docker)
   - Cloud databases (AWS RDS)
   - Performance optimization
""")

print("\n" + "="*60 + "\n🎉 CONGRATS ON COMPLETING DAY 6! 🎉\n" + "="*60)