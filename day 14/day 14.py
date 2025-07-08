"""
🚀 PYTHON DAY 14: BUILDING APIS WITH DJANGO REST FRAMEWORK 🚀
Covers:
1. DRF Setup & Serializers
2. Viewsets & Routers
3. Authentication & Permissions
4. Documentation
5. Capstone Project
"""

# ================ 1. DRF SETUP & SERIALIZERS ================
print("\n" + "="*60 + "\n🌐 1. DRF FUNDAMENTALS\n" + "="*60)

# Install DRF first (run in terminal):
print("\nFirst install DRF:")
print("pip install djangorestframework")

# Add to INSTALLED_APPS in settings.py:
INSTALLED_APPS = [
    ...,
    'rest_framework',
    'rest_framework.authtoken',  # For token auth
]

# blog/serializers.py
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at']
        read_only_fields = ['created_at']

# ================ 2. VIEWSETS & ROUTERS ================
print("\n" + "="*60 + "\n🔄 2. VIEWSETS & ROUTERS\n" + "="*60)

# blog/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAuthorOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# blog/permissions.py
from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

# blog/urls.py
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('api/', include(router.urls)),
]

# ================ 3. AUTHENTICATION ================
print("\n" + "="*60 + "\n🔐 3. API AUTHENTICATION\n" + "="*60)

# settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ]
}

# users/views.py (for token auth)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

# users/urls.py
urlpatterns = [
    path('api-token-auth/', CustomAuthToken.as_view()),
]

# ================ 4. DOCUMENTATION ================
print("\n" + "="*60 + "\n📝 4. API DOCUMENTATION\n" + "="*60)

# Install required packages:
print("\nInstall documentation tools:")
print("pip install drf-yasg")

# Add to INSTALLED_APPS:
INSTALLED_APPS += ['drf_yasg']

# project/urls.py
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Blog API",
      default_version='v1',
      description="API documentation for our blog",
   ),
   public=True,
)

urlpatterns += [
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0)),
]

# ================ 5. CAPSTONE PROJECT ================
print("\n" + "="*60 + "\n🏆 5. BUILD A SOCIAL MEDIA API\n" + "="*60)

"""
🔧 Features to Implement:
1. User profiles API
2. Post creation with images
3. Like/comment functionality
4. Follow system
5. JWT authentication

📁 Suggested Models:
- Profile (OneToOne with User)
- Post (with image field)
- Comment
- Like
- Follow
"""

# Example model for comments
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class CommentSerializer(serializers.ModelSerializer):
    class Meta: