from django.shortcuts import render
from .forms import NoteForm
from .models import Note, Status, Category

from django.shortcuts import render, get_object_or_404, redirect
from .models import Note, User, Status, Category



def notes_list(request):
    status_id = request.GET.get("status")
    category_id = request.GET.get("category")

    notes = (
        Note.objects
        .select_related("author", "status", "category")
        .all()
    )

    
    if status_id:
        notes = notes.filter(status_id=status_id)

    
    if category_id:
        notes = notes.filter(category_id=category_id)

    statuses = Status.objects.all()
    categories = Category.objects.all()

    context = {
        "notes": notes,
        "statuses": statuses,
        "categories": categories,
        "selected_status": status_id,
        "selected_category": category_id,
    }

    return render(request, "notes_app/notes_list.html", context)



def note_detail(request, note_id):
    note = get_object_or_404(Note, id=note_id)

    return render(request, "notes_app/note_detail.html", {"note": note})



def user_detail(request, user_id):
    user_obj = get_object_or_404(User, id=user_id)

    notes = user_obj.notes.select_related("status", "category")

    return render(
        request,
        "notes_app/user_detail.html",
        {"user_obj": user_obj, "notes": notes}
    )



def users_list(request):
    users = User.objects.all()
    return render(request, "notes_app/users_list.html", {"users": users})



def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("notes_list")  # имя твоего списка заметок
    else:
        form = NoteForm()

    return render(request, "notes_app/note_form.html", {"form": form})



def note_edit(request, note_id):
    note = get_object_or_404(Note, id=note_id)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("note_detail", note_id=note.id)
    else:
        form = NoteForm(instance=note)

    return render(request, "notes_app/note_form.html", {"form": form})



def note_delete(request, note_id):
    note = get_object_or_404(Note, id=note_id)

    if request.method == "POST":
        note.delete()
        return redirect("notes_list")

    return render(request, "notes_app/note_confirm_delete.html", {"note": note})