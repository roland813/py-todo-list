from django.urls import path

from tags.views import Index, TagListView, TagCreateView, TagUpdateView, TagDeleteView, \
    TaskDeleteView, TaskCreateView, TaskUpdateView, change_button

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path('tags/', TagListView.as_view(), name='tags'),
    path('tags/create_tag/', TagCreateView.as_view(), name='tag_create'),
    path('tags/update/<int:pk>/', TagUpdateView.as_view(), name='tag_update'),
    path('tags/delete/<int:pk>/', TagDeleteView.as_view(), name='tag_delete'),
    path("todo/<int:pk>/change", change_button, name="change-button"),
    path('create_task/', TaskCreateView.as_view(), name='task_create'),
    path('delete_task/<int:pk>', TaskDeleteView.as_view(), name='task_delete'),
    path('update_task/<int:pk>', TaskUpdateView.as_view(), name='task_update'),
]

app_name = "tags"
