
from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView


urlpatterns = [
    path('', include('catalog.urls')),
    path("graphql", GraphQLView.as_view(graphiql=True)),
    path('admin/', admin.site.urls),
]
