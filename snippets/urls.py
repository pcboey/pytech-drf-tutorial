from django.conf.urls import url, include
from snippets import views
from rest_framework.routers import DefaultRouter

##########################################################################################
##
## pytech-drf-tutorial step-12
## Using Routers
## See http://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/#using-routers
##
##########################################################################################

# Create a router and register our viewsets with it.
# The DefaultRouter class also automatically creates the API root view for us
# so we can now delete the api_root method from our views module.

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
