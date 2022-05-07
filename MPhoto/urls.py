from unicodedata import name
from django.contrib import admin
from django.urls import path
from .views import upload_progress_image, photo_add_view, staging_image, PhotoListView, PhotoJsonView
urlpatterns = [
     path('photo_upload/', photo_add_view, name="photo-view"),
     path('photo_upload_progress', upload_progress_image, name="photo-progress-view"),
     path('stagingimage/', staging_image, name="staging-image"),
     path('photo_list/', PhotoListView.as_view(), name="photo-list-view" ),
     path('photo_json_view', PhotoJsonView.as_view(), name="photo-json-view"),
]
