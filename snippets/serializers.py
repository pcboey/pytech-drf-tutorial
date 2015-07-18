from rest_framework import serializers

from .models import Snippet

################################################################################
## Using ModelSerializers
## No Authentication and Permissions
## Anyone can edit or delete code snippets
## See http://www.django-rest-framework.org/tutorial/1-serialization/   Using ModelSerializers
################################################################################
 
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')
