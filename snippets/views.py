from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework import permissions

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

#########################################################################################
## pytech-drf-tutorial step-7
## See http://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/#adding-endpoints-for-our-user-models
## Use ListAPIView and RetrieveAPIView generic class based views to add some views
#########################################################################################

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
