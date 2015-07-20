from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics

#########################################################################################
## pytech-drf-tutorial step-6
## Using generic class based views
## See http://www.django-rest-framework.org/tutorial/3-class-based-views/#using-generic-class-based-views

## WE REALLY SAVE A LOT OF CODE!!!
#########################################################################################

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

