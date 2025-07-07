"""
🚀 PYTHON DAY 13: FULL-STACK DEVELOPMENT WITH DJANGO 🚀
Covers:
1. Django Project Setup
2. Models & Admin Panel
3. Views & Templates
4. User Authentication
5. Deployment
"""

# ================ 1. DJANGO PROJECT SETUP ================
print("\n" + "="*60 + "\n🌐 1. DJANGO PROJECT SETUP\n" + "="*60)

"""
🔍 Django Structure:
- Project: Container for multiple apps
- Apps: Modular components (e.g., blog, users)
- MTV Pattern: Model-Template-View (Django's MVC)
"""

# 🛠️ Command Line Setup (Run these in terminal)
print("\nRun these commands to set up:")
print("""
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\\Scripts\\activate    # Windows

# Install Django
pip install django

# Create project and app
django-admin startproject myproject
cd myproject
python manage.py startapp blog
""")

# ================ 2. MODELS & ADMIN PANEL ================
print("\n" + "="*60 + "\n💾 2. MODELS & ADMIN\n" + "="*60)

# blog/models.py
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# blog/admin.py
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'content')

admin.site.register(Post, PostAdmin)

print("\nAfter creating models, run:")
print("""
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
""")

# ================ 3. VIEWS & TEMPLATES ================
print("\n" + "="*60 + "\n🖥️ 3. VIEWS & TEMPLATES\n" + "="*60)

# blog/views.py
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post

# blog/urls.py
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]

print("\nTemplate example (blog/templates/blog/home.html):")
print("""
{% for post in posts %}
    <article>
        <h2>{{ post.title }}</h2>
        <p>By {{ post.author }} on {{ post.created_at|date:"F j, Y" }}</p>
        <p>{{ post.content }}</p>
    </article>
{% endfor %}
""")

# ================ 4. USER AUTHENTICATION ================
print("\n" + "="*60 + "\n🔐 4. USER AUTHENTICATION\n" + "="*60)

# myproject/urls.py
urlpatterns += [
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]

# users/views.py
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# users/forms.py
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# ================ 5. DEPLOYMENT ================
print("\n" + "="*60 + "\n🚀 5. DEPLOYMENT\n" + "="*60)

print("\nDeploy to Heroku:")
print("""
1. Create requirements.txt
pip freeze > requirements.txt

2. Create Procfile
web: gunicorn myproject.wsgi

3. Create runtime.txt
python-3.9.7

4. Push to Heroku
heroku create
git push heroku master
heroku run python manage.py migrate
""")

# ================ 🏆 6. CAPSTONE PROJECT ================
print("\n" + "="*60 + "\n🏆 6. BUILD A BLOG PLATFORM\n" + "="*60)

"""
🔧 Features to Implement:
1. User registration/login
2. CRUD for blog posts
3. Comment system
4. Profile pages
5. Deployment

📁 Project Structure:
myproject/
├── blog/
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   └── urls.py
├── users/
│   ├── forms.py
│   └── views.py
├── static/
├── media/
└── myproject/
"""

# ================ 🚀 7. NEXT STEPS ================
print("\n" + "="*60 + "\n🚀 7. WHAT TO LEARN NEXT\n" + "="*60)
print("""
1. Advanced Django:
   - REST APIs with Django REST Framework
   - WebSockets with Django Channels
   - Custom middleware

2. Frontend Integration:
   - React/Vue with Django
   - HTMX for modern interactivity
   - Tailwind CSS styling

3. Scaling:
   - PostgreSQL setup
   - Caching with Redis
   - Celery for background tasks
""")

if __name__ == "__main__":
    print("\n" + "="*60 + "\n🎉 RUN THESE COMMANDS TO START YOUR DJANGO PROJECT!\n" + "="*60)