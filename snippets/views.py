from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework import permissions

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from snippets.permissions import IsOwnerOrReadOnly

#########################################################################################
## pytech-drf-tutorial step-12
## Using Routers
##    
## See http://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/#using-routers
## The DefaultRouter class in urls.py also automatically creates the API root view for us
## so we can now delete the api_root method from our views module.
#########################################################################################

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

class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
            serializer.save(owner=self.request.user)
