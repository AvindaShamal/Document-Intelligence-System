from django.urls import path
from .views import (
    DocumentUploadView,
    DocumentListView,
    DocumentDetailView,
    SemanticSearchView,
)

urlpatterns = [
    path("upload/", DocumentUploadView.as_view(), name="document-upload"),
    path("list/", DocumentListView.as_view(), name="document-list"),
    path("detail/<int:pk>/", DocumentDetailView.as_view(), name="document-detail"),
    path("search/", SemanticSearchView.as_view(), name="semantic-search"),
]
