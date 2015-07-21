from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Snippet

################################################################################
## Step 10 Relationships & Hyperlinked APIs
## 
## See http://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/#updating-our-serializer
################################################################################
 
## Hyperlinking our API
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'snippets')
