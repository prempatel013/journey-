"""
🚀 PYTHON DAY 8: ADVANCED PYTHON TECHNIQUES 🚀
Covers:
1. Async/Await Programming
2. WebSockets with FastAPI
3. Unit Testing & Debugging
4. Performance Optimization
"""

# ================ 1. ASYNC/AWAIT PROGRAMMING ================
print("\n" + "="*60 + "\n⏳ 1. ASYNCHRONOUS PYTHON\n" + "="*60)

import asyncio
import aiohttp

"""
🔍 Async Basics:
- Concurrent execution without threads
- Ideal for I/O-bound tasks
- Uses 'async' and 'await' keywords
"""

# 🛠️ Example 1: Basic Coroutine
async def greet(name):
    await asyncio.sleep(1)  # Simulate I/O operation
    return f"Hello, {name}!"

async def run_greetings():
    tasks = [
        greet("Alice"),
        greet("Bob"),
        greet("Charlie")
    ]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)

# Run the async example
print("Async Greetings:")
asyncio.run(run_greetings())

# 🛠️ Example 2: Concurrent HTTP Requests
async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def fetch_multiple():
    urls = [
        "https://python.org",
        "https://fastapi.tiangolo.com",
        "https://docs.aiohttp.org"
    ]
    tasks = [fetch_url(url) for url in urls]
    pages = await asyncio.gather(*tasks)
    print(f"Fetched {len(pages)} pages concurrently")

print("\nFetching web pages:")
asyncio.run(fetch_multiple())

# ================ 2. WEBSOCKETS WITH FASTAPI ================
print("\n" + "="*60 + "\n🔌 2. REALTIME WITH WEBSOCKETS\n" + "="*60)

from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

"""
🔍 WebSockets:
- Persistent two-way connections
- Ideal for chat apps, realtime updates
- Works with FastAPI or other ASGI servers
"""

app = FastAPI()

# HTML page for testing WebSocket
html = """
<!DOCTYPE html>
<html>
    <head>
        <title>WebSocket Test</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            const ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                const messages = document.getElementById('messages')
                const message = document.createElement('li')
                message.innerText = event.data
                messages.appendChild(message)
            };
            function sendMessage(event) {
                const input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""

@app.get("/")
async def get():
    return HTMLResponse(html)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Echo: {data}")

# To run:
# uvicorn day8:app --reload
# Then visit http://localhost:8000

# ================ 3. TESTING & DEBUGGING ================
print("\n" + "="*60 + "\n🧪 3. TESTING & DEBUGGING\n" + "="*60)

import unittest
from unittest.mock import patch

"""
🔍 Testing Pyramid:
- Unit tests (fast, isolated)
- Integration tests (service interactions)
- E2E tests (full system)
"""

# 🛠️ Example 3: Unit Testing
def calculate_discount(price, discount_percent):
    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100")
    return price * (1 - discount_percent / 100)

class TestDiscount(unittest.TestCase):
    def test_normal_discount(self):
        self.assertEqual(calculate_discount(100, 20), 80)
    
    def test_invalid_discount(self):
        with self.assertRaises(ValueError):
            calculate_discount(100, 120)

# 🛠️ Example 4: Mocking API Calls
class APIClient:
    def get_data(self):
        # Simulate expensive API call
        return {"status": "success", "data": [1, 2, 3]}

class TestAPIClient(unittest.TestCase):
    @patch.object(APIClient, 'get_data')
    def test_api_client(self, mock_get):
        mock_get.return_value = {"status": "mocked"}
        client = APIClient()
        result = client.get_data()
        self.assertEqual(result["status"], "mocked")

# Run tests
print("Running tests:")
unittest.main(argv=[''], exit=False)

# ================ 4. PERFORMANCE OPTIMIZATION ================
print("\n" + "="*60 + "\n⚡ 4. PERFORMANCE TECHNIQUES\n" + "="*60)

import timeit
from functools import lru_cache

"""
🔍 Optimization Strategies:
- Caching
- Algorithm selection
- Profiling before optimizing
"""

# 🛠️ Example 5: Memoization
@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("\nFibonacci with caching:")
print(f"fib(30) = {fibonacci(30)}")

# 🛠️ Example 6: Profiling
def slow_function():
    total = 0
    for i in range(10**6):
        total += i
    return total

print("\nPerformance measurement:")
execution_time = timeit.timeit(slow_function, number=10)
print(f"10 executions took {execution_time:.4f} seconds")

# ================ 🏆 5. CAPSTONE PROJECT ================
print("\n" + "="*60 + "\n🏆 5. REAL-TIME DASHBOARD\n" + "="*60)

from fastapi import WebSocketDisconnect
import random
import json

@app.websocket("/dashboard")
async def dashboard_websocket(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # Simulate realtime data
            data = {
                "temperature": random.uniform(18, 25),
                "humidity": random.uniform(30, 70),
                "timestamp": time.time()
            }
            await websocket.send_json(data)
            await asyncio.sleep(1)  # Update every second
    except WebSocketDisconnect:
        print("Client disconnected")

"""
To test:
1. Run with: uvicorn day8:app --reload
2. Visit http://localhost:8000
3. Open browser console and run:
   const ws = new WebSocket("ws://localhost:8000/dashboard")
   ws.onmessage = (event) => console.log(JSON.parse(event.data))
"""

# ================ 🚀 6. CONTINUING JOURNEY ================
print("\n" + "="*60 + "\n🚀 6. WHAT TO LEARN NEXT\n" + "="*60)
print("""
1. Advanced Async:
   - asyncio internals
   - Async database drivers
   - Distributed task queues (Celery)

2. Production Deployment:
   - Docker containers
   - Kubernetes orchestration
   - Load testing (Locust)

3. Architecture:
   - Microservices design
   - Event-driven systems
   - CQRS pattern

4. Specialized Libraries:
   - NumPy/SciPy for scientific computing
   - PyTorch/TensorFlow for ML
   - Pandas for data analysis
""")

if __name__ == "__main__":
    print("\n" + "="*60 + "\n🎉 RUN ALL DAY 8 EXAMPLES\n" + "="*60)