from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Snippet

################################################################################
## Step 8 Associating Snippets with Users
## 
## See http://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/#updating-our-serializer
################################################################################
 
class SnippetSerializer(serializers.ModelSerializer):
    # 
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')
