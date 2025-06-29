"""
🌟 PYTHON API & SCRAPING BOOTCAMP 🌟
A complete journey from beginner to professional in 7 levels
"""

# ==================== 🧩 LEVEL 1: HELLO API ====================
print("\n" + "="*60 + "\n🧩 LEVEL 1: Your First API Call\n" + "="*60)

# The simplest possible API request
import time
import requests

response = requests.get("https://api.github.com")
print(f"GitHub API status: {response.status_code}")
print(f"Response snippet: {response.text[:100]}...")

"""
📚 Learning Checklist:
✅ What's an API endpoint
✅ HTTP status codes
✅ Viewing raw API responses
"""

# ==================== 📚 LEVEL 2: WORKING WITH JSON ====================
print("\n" + "="*60 + "\n📚 LEVEL 2: Parsing API Responses\n" + "="*60)

# Get JSON data from a public API
astronauts = requests.get("http://api.open-notify.org/astros.json").json()

print("\nCurrent astronauts in space:")
for person in astronauts["people"]:
    print(f"• {person['name']} on {person['craft']}")

"""
📚 Learning Checklist:
✅ response.json() method
✅ Navigating JSON structures
✅ Looping through API data
"""

# ==================== 🔐 LEVEL 3: API AUTHENTICATION ====================
print("\n" + "="*60 + "\n🔐 LEVEL 3: Secured APIs\n" + "="*60)

# Simulating API key usage (in real projects, use environment variables!)
def get_weather(city):
    # This is a simulation - real API would need actual key
    mock_data = {
        "London": {"temp": 18, "conditions": "cloudy"},
        "Paris": {"temp": 22, "conditions": "sunny"}
    }
    return mock_data.get(city, {})

print("London weather:", get_weather("London"))

"""
📚 Learning Checklist:
✅ API keys and authentication
✅ Environment variables for secrets
✅ Mocking APIs for testing
"""

# ==================== 🕷️ LEVEL 4: WEB SCRAPING BASICS ====================
print("\n" + "="*60 + "\n🕷️ LEVEL 4: Your First Web Scraper\n" + "="*60)

from bs4 import BeautifulSoup

# Scrape book titles from practice site
html = requests.get("http://books.toscrape.com").text
soup = BeautifulSoup(html, "html.parser")

print("\nTop 3 books:")
for book in soup.select("article.product_pod")[:3]:
    title = book.h3.a["title"]
    price = book.select_one("p.price_color").text
    print(f"• {title} ({price})")

"""
📚 Learning Checklist:
✅ BeautifulSoup installation
✅ HTML structure navigation
✅ CSS selector basics
"""

# ==================== 🤖 LEVEL 5: DYNAMIC SCRAPING ====================
print("\n" + "="*60 + "\n🤖 LEVEL 5: JavaScript-Rendered Pages\n" + "="*60)

# Selenium example (commented out as it needs browser setup)
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

try:
    driver.get("https://quotes.toscrape.com/js/")
    quote = driver.find_element(By.CLASS_NAME, "text").text
    print(f"First JavaScript-rendered quote: {quote}")
finally:
    driver.quit()
"""

print("\nNote: Uncomment the Selenium code after installing:")
print("1. pip install selenium")
print("2. Download ChromeDriver")

"""
📚 Learning Checklist:
✅ When to use Selenium
✅ Headless browser mode
✅ Element location strategies
"""

# ==================== 🚀 LEVEL 6: PRODUCTION-READY APIS ====================
print("\n" + "="*60 + "\n🚀 LEVEL 6: Professional API Client\n" + "="*60)

class ProfessionalAPIClient:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "MyApp/1.0",
            "Accept": "application/json"
        })
    
    def get_with_retry(self, url, max_retries=3):
        for attempt in range(max_retries):
            try:
                response = self.session.get(url, timeout=5)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                print(f"Attempt {attempt+1} failed: {str(e)}")
                if attempt == max_retries - 1:
                    raise
                time.sleep(2 ** attempt)  # Exponential backoff

# Usage example:
client = ProfessionalAPIClient()
# data = client.get_with_retry("https://api.example.com/data")

"""
📚 Learning Checklist:
✅ Session management
✅ Exponential backoff
✅ Proper headers
✅ Timeout handling
"""

# ==================== 💼 LEVEL 7: REAL-WORLD PROJECT ====================
print("\n" + "="*60 + "\n💼 LEVEL 7: Job Market Analyzer\n" + "="*60)

class JobMarketAnalyzer:
    def __init__(self):
        self.skills = ["Python", "JavaScript", "SQL"]
    
    def analyze(self):
        print("\n💡 Job Market Insights:")
        
        # Simulated API and scraping results
        results = {
            "Python": {"demand": "High", "avg_salary": "$110,000"},
            "JavaScript": {"demand": "Very High", "avg_salary": "$105,000"},
            "SQL": {"demand": "Medium", "avg_salary": "$95,000"}
        }
        
        for skill in self.skills:
            data = results.get(skill, {})
            print(f"{skill}:")
            print(f"  • Demand: {data.get('demand', 'Unknown')}")
            print(f"  • Avg Salary: {data.get('avg_salary', 'N/A')}")

# Run analysis
JobMarketAnalyzer().analyze()

"""
📚 Learning Checklist:
✅ Combining APIs with scraping
✅ Data analysis basics
✅ Presenting insights
"""

# ==================== 🎓 CONTINUING EDUCATION ====================
print("\n" + "="*60 + "\n🎓 Where To Go Next\n" + "="*60)
print("""
1. Advanced APIs:
   - OAuth authentication
   - Webhooks
   - GraphQL

2. Professional Scraping:
   - Scrapy framework
   - Proxy rotation
   - CAPTCHA solving

3. Deployment:
   - Docker containers
   - AWS Lambda
   - Scheduled scraping

4. Specialize:
   ↗️ Data Science APIs (Pandas, NumPy)
   ↗️ Web Automation (Playwright)
   ↗️ API Development (FastAPI)
""")

print("\n" + "="*60 + "\n🎉 CONGRATS! YOU'RE NOW API & SCRAPING PRO! 🎉\n" + "="*60)