from django.urls import path
from .views import notes_list, note_detail, users_list, user_detail

urlpatterns = [
    path("", notes_list, name="notes_list"),

    # Заметки
    path("notes/<int:note_id>/", note_detail, name="note_detail"),

    # Пользователи
    path("users/", users_list, name="users_list"),      # список пользователей
    path("users/<int:user_id>/", user_detail, name="user_detail"),  # детальная страница
]