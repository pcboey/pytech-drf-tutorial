from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework import permissions

# Add these imports
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
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


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#########################################################################################
## pytech-drf-tutorial step-10
## Relationships & Hyperlinked APIs
##    
## See http://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis/
#########################################################################################

## Create an endpoint for the root of our API
@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })

## Create endpoint for highlighted snippets
class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
