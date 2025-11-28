from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название категории"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(verbose_name="Email")
    bio = models.TextField(blank=True, verbose_name="О себе")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=100, verbose_name="Статус")
    is_final = models.BooleanField(default=False, verbose_name="Финальный статус")

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

    def __str__(self):
        return self.name


class Note(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Название"
    )
    content = models.TextField(
        verbose_name="Содержимое"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="notes",
        null=True,
        blank=True,
        verbose_name="Категория"
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notes",
        null=True,
        blank=True,
        verbose_name="Автор"
    )

    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        related_name="notes",
        null=True,
        blank=True,
        verbose_name="Статус"
    )

    class Meta:
        verbose_name = "Заметка"
        verbose_name_plural = "Заметки"

    def __str__(self):
        return self.title