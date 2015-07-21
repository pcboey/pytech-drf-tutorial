from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Snippet

################################################################################
## Authentication & Permissions
## Adding endpoints for our User models
## 
## See http://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/#adding-endpoints-for-our-user-models
################################################################################
 
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')
