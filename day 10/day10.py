"""
🚀 PYTHON DAY 10: ADVANCED PYTHON TECHNIQUES 🚀
Covers:
1. Advanced Decorators
2. Generator Patterns
3. Context Managers
4. Metaprogramming
5. Capstone Project
"""

# ================ 1. ADVANCED DECORATORS ================
print("\n" + "="*60 + "\n✨ 1. ADVANCED DECORATORS\n" + "="*60)

"""
🔍 Decorator Deep Dive:
- Decorators with arguments
- Class decorators
- Decorator stacking
"""

# 🛠️ Example 1: Decorator with Arguments
def retry(max_attempts=3, delay=1):
    def decorator(func):
        import time
        from functools import wraps
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Attempt {attempts} failed: {str(e)}")
                    if attempts < max_attempts:
                        time.sleep(delay)
            raise RuntimeError(f"Failed after {max_attempts} attempts")
        return wrapper
    return decorator

@retry(max_attempts=5, delay=2)
def unreliable_api_call():
    import random
    if random.random() < 0.7:  # 70% chance of failure
        raise ValueError("API timeout")
    return "Success"

print("Retry decorator example:")
try:
    print(unreliable_api_call())
except RuntimeError as e:
    print(e)

# 🛠️ Example 2: Class Decorator
def singleton(cls):
    instances = {}
    
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singleton
class DatabaseConnection:
    def __init__(self):
        print("Establishing database connection...")

print("\nSingleton pattern demo:")
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(f"Same instance? {db1 is db2}")

# ================ 2. GENERATOR PATTERNS ================
print("\n" + "="*60 + "\n🌀 2. GENERATOR PATTERNS\n" + "="*60)

"""
🔍 Generator Techniques:
- Infinite sequences
- Pipeline processing
- Coroutine-based generators
"""

# 🛠️ Example 3: Infinite Sequence Generator
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

print("\nFibonacci sequence (first 10):")
fib = fibonacci()
for _ in range(10):
    print(next(fib), end=" ")
print()

# 🛠️ Example 4: Generator Pipeline
def read_files(filenames):
    for filename in filenames:
        with open(filename) as f:
            yield f.read()

def filter_lines(texts, pattern):
    import re
    for text in texts:
        for line in text.split('\n'):
            if re.search(pattern, line):
                yield line

print("\nGenerator pipeline example (simulated):")
files = ["data1.txt", "data2.txt"]  # Would be real files
lines = filter_lines(read_files(files), r"error")
for line in lines:
    print(line)

# ================ 3. CONTEXT MANAGERS ================
print("\n" + "="*60 + "\n🔌 3. ADVANCED CONTEXT MANAGERS\n" + "="*60)

"""
🔍 Beyond 'with' Statements:
- Class-based context managers
- Contextlib utilities
- Handling exceptions
"""

# 🛠️ Example 5: Class-Based Context Manager
class Timer:
    def __enter__(self):
        import time
        self.start = time.perf_counter()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.elapsed = time.perf_counter() - self.start
        print(f"Operation took {self.elapsed:.4f} seconds")
        if exc_type is not None:
            print(f"Exception occurred: {exc_val}")
        return True  # Suppress exceptions

print("\nTiming context manager:")
with Timer() as t:
    sum(range(10**6))
    # raise ValueError("Test error")  # Uncomment to test exception handling

# 🛠️ Example 6: Contextlib for Resource Management
from contextlib import contextmanager

@contextmanager
def temporary_file(content):
    import tempfile
    temp = tempfile.NamedTemporaryFile(delete=False)
    try:
        temp.write(content.encode())
        temp.close()
        yield temp.name
    finally:
        import os
        os.unlink(temp.name)

print("\nTemporary file context:")
with temporary_file("Test content") as temp_path:
    print(f"Created temp file at {temp_path}")
    with open(temp_path) as f:
        print(f"Content: {f.read()}")

# ================ 4. METAPROGRAMMING ================
print("\n" + "="*60 + "\n🧙 4. METAPROGRAMMING\n" + "="*60)

"""
🔍 Python Magic:
- Dynamic attribute access
- Class creation at runtime
- Monkey patching
"""

# 🛠️ Example 7: Dynamic Attribute Access
class DynamicAttributes:
    def __getattr__(self, name):
        if name.startswith('fake_'):
            def method(*args):
                print(f"Fake method '{name}' called with {args}")
            return method
        raise AttributeError(f"No attribute {name}")

print("\nDynamic attributes demo:")
dyn = DynamicAttributes()
dyn.fake_operation(1, 2, 3)  # Created at runtime

# 🛠️ Example 8: Class Factory
def class_factory(class_name, **attributes):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
    
    cls_dict = {'__init__': __init__}
    cls_dict.update(attributes)
    
    return type(class_name, (object,), cls_dict)

print("\nClass factory demo:")
Dog = class_factory("Dog", bark=lambda self: print("Woof!"))
spot = Dog(name="Spot")
print(f"Created {spot.name}")
spot.bark()

# ================ 🏆 5. CAPSTONE PROJECT ================
print("\n" + "="*60 + "\n🏆 5. DATA PROCESSING PIPELINE\n" + "="*60)

import time
from collections import Counter
from contextlib import contextmanager

class DataPipeline:
    def __init__(self):
        self.processors = []
    
    def add_processor(self, func):
        self.processors.append(func)
        return self  # Allow chaining
    
    def process(self, data):
        for processor in self.processors:
            data = processor(data)
        return data

@contextmanager
def pipeline_timer(name):
    start = time.perf_counter()
    yield
    elapsed = time.perf_counter() - start
    print(f"{name} took {elapsed:.4f} seconds")

print("\nBuilding data pipeline...")

# Create pipeline
pipeline = (DataPipeline()
    .add_processor(lambda data: [x.strip() for x in data])
    .add_processor(lambda data: [x for x in data if x])
    .add_processor(lambda data: [x.upper() for x in data])
    .add_processor(lambda data: Counter(data))
)

# Test data
test_data = [" apple ", "banana ", "", "  apple", "orange", "banana"]

with pipeline_timer("Processing"):
    result = pipeline.process(test_data)
    print("Processed result:", result)

# ================ 🚀 6. CONTINUING JOURNEY ================
print("\n" + "="*60 + "\n🚀 6. WHAT TO LEARN NEXT\n" + "="*60)
print("""
1. Concurrency:
   - Asyncio advanced patterns
   - Multithreading vs multiprocessing
   - Distributed computing

2. Performance:
   - Cython for speed
   - Profiling with cProfile
   - Memory optimization

3. Architecture:
   - Design patterns in Python
   - Microservices
   - Event-driven systems

4. Specialization:
   ↗️ Web Development (Django, FastAPI)
   ↗️ Data Science (Pandas, NumPy, SciPy)
   ↗️ Machine Learning (PyTorch, TensorFlow)
""")

print("\n" + "="*60 + "\n🎉 CONGRATS ON COMPLETING 10 DAYS OF PYTHON! 🎉\n" + "="*60)