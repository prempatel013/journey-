"""
🚀 PYTHON DAY 12: BUILDING PRODUCTION APIS WITH FASTAPI 🚀
Covers:
1. FastAPI Fundamentals
2. Database Integration
3. Authentication & Security
4. Testing & Deployment
"""

# ================ 1. FASTAPI FUNDAMENTALS ================
print("\n" + "="*60 + "\n🌐 1. FASTAPI FUNDAMENTALS\n" + "="*60)

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, EmailStr
from typing import Optional, List
import uuid
from datetime import datetime

app = FastAPI(
    title="Task Manager API",
    description="A production-ready task management system",
    version="0.1.0",
    docs_url="/docs",
    redoc_url=None
)

# Sample data store (replace with real DB later)
tasks_db = []
users_db = []

# 🛠️ Example 1: Basic CRUD Endpoints
class Task(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class TaskInDB(Task):
    id: str
    owner_id: str
    created_at: datetime
    updated_at: datetime

@app.post("/tasks/", response_model=TaskInDB, status_code=status.HTTP_201_CREATED)
async def create_task(task: Task, user_id: str = "demo-user"):
    """Create a new task"""
    task_data = task.dict()
    task_id = str(uuid.uuid4())
    now = datetime.utcnow()
    db_task = TaskInDB(
        **task_data,
        id=task_id,
        owner_id=user_id,
        created_at=now,
        updated_at=now
    )
    tasks_db.append(db_task)
    return db_task

@app.get("/tasks/", response_model=List[TaskInDB])
async def list_tasks(limit: int = 10, offset: int = 0):
    """List all tasks with pagination"""
    return tasks_db[offset:offset + limit]

# ================ 2. DATABASE INTEGRATION ================
print("\n" + "="*60 + "\n💾 2. DATABASE INTEGRATION\n" + "="*60)

from sqlalchemy import create_engine, Column, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite Database Setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./taskmanager.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database Models
class DBUser(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

class DBTask(Base):
    __tablename__ = "tasks"
    id = Column(String, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    completed = Column(Boolean, default=False)
    owner_id = Column(String, index=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

# Create tables
Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 🛠️ Example 2: Database CRUD Operations
@app.post("/db-tasks/", response_model=TaskInDB)
async def create_db_task(task: Task, db=Depends(get_db), user_id: str = "demo-user"):
    """Create task with database storage"""
    db_task = DBTask(
        id=str(uuid.uuid4()),
        **task.dict(),
        owner_id=user_id,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# ================ 3. AUTHENTICATION & SECURITY ================
print("\n" + "="*60 + "\n🔐 3. AUTHENTICATION SYSTEM\n" + "="*60)

from passlib.context import CryptContext # type: ignore
from jose import JWTError, jwt   # type: ignore
from datetime import timedelta

# Security config
SECRET_KEY = "your-secret-key-here"  # In production, use environment variables
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserInDB(BaseModel):
    id: str
    email: EmailStr
    hashed_password: str
    is_active: bool

class Token(BaseModel):
    access_token: str
    token_type: str

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@app.post("/register/", response_model=UserInDB)
async def register_user(user: UserCreate, db=Depends(get_db)):
    """Register a new user"""
    hashed_password = get_password_hash(user.password)
    db_user = DBUser(
        id=str(uuid.uuid4()),
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# ================ 4. TESTING & DEPLOYMENT ================
print("\n" + "="*60 + "\n🚀 4. TESTING & DEPLOYMENT\n" + "="*60)

# 🛠️ Example 3: Automated Tests
from fastapi.testclient import TestClient
import pytest # type: ignore

client = TestClient(app)

def test_create_task():
    response = client.post(
        "/tasks/",
        json={"title": "Test Task", "description": "Test Description"}
    )
    assert response.status_code == 201
    assert response.json()["title"] == "Test Task"

# 🛠️ Example 4: Deployment Options
print("\nDeployment Options:")
print("""
1. Local Development:
   uvicorn main:app --reload

2. Production with Gunicorn:
   gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app

3. Docker Example:
   # Dockerfile
   FROM python:3.9
   COPY . /app   
   WORKDIR /app
   RUN pip install -r requirements.txt
   CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app"]
""")

# ================ 🏆 5. CAPSTONE PROJECT ================
print("\n" + "="*60 + "\n🏆 5. COMPLETE TASK MANAGER API\n" + "="*60)

class TaskUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    completed: Optional[bool]

@app.put("/tasks/{task_id}", response_model=TaskInDB)
async def update_task(task_id: str, task_update: TaskUpdate, db=Depends(get_db)):
    """Update a task"""
    db_task = db.query(DBTask).filter(DBTask.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    update_data = task_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_task, field, value)
    db_task.updated_at = datetime.utcnow()
    
    db.commit()
    db.refresh(db_task)
    return db_task

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: str, db=Depends(get_db)):
    """Delete a task"""
    db_task = db.query(DBTask).filter(DBTask.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    db.delete(db_task)
    db.commit()
    return None

# ================ 🚀 6. NEXT STEPS ================
print("\n" + "="*60 + "\n🚀 6. BEYOND THE BASICS\n" + "="*60)
print("""
1. Advanced Features:
   - Background tasks
   - WebSocket endpoints
   - Dependency injection
   - Custom middleware

2. Scaling:
   - Database connection pooling
   - Caching with Redis
   - Load balancing

3. Monitoring:
   - Prometheus metrics
   - Logging configuration
   - Health checks

4. Frontend Integration:
   - CORS configuration
   - OpenAPI documentation
   - Swagger UI customization
""")

if __name__ == "__main__":
    import uvicorn 
    print("\n" + "="*60 + "\n🌍 STARTING DEVELOPMENT SERVER\n" + "="*60)
    uvicorn.run(app, host="0.0.0.0", port=8000)