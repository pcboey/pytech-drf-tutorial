from django.contrib.auth.models import User

from rest_framework import generics

from rest_framework import permissions

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer

# Add this import
from snippets.permissions import IsOwnerOrReadOnly

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # Add this property
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    ## Step 8 - Associating Snippets with Users
    ## Override perform_create method to modify the instance save
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # Edit the property to include IsOwnerOrReadOnly
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

#########################################################################################
## pytech-drf-tutorial step-9
## Object level permissions
## See http://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/#object-level-permissions
#########################################################################################

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
