from django.urls import path
from .views import (
    notes_list,
    note_detail,
    users_list,
    user_detail,
    note_create,
    note_edit,
    note_delete,
)

urlpatterns = [
    # Главная страница со списком заметок
    path("", notes_list, name="notes_list"),

    # Заметки (детальная)
    path("notes/<int:note_id>/", note_detail, name="note_detail"),

    # --- CRUD ---
    path("notes/create/", note_create, name="note_create"),
    path("notes/<int:note_id>/edit/", note_edit, name="note_edit"),
    path("notes/<int:note_id>/delete/", note_delete, name="note_delete"),
    # -------------

    # Пользователи
    path("users/", users_list, name="users_list"),
    path("users/<int:user_id>/", user_detail, name="user_detail"),
]