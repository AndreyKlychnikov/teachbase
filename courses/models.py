from django.db import models


class ContentType(models.IntegerChoices):
    COURSE = 1
    QUIZ = 2
    LITERATURE = 3


class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner_id = models.BigIntegerField()
    owner_name = models.CharField(max_length=255)
    thumb_url = models.URLField()
    description = models.TextField()
    total_score = models.IntegerField()
    total_tasks = models.IntegerField()
    unchangeable = models.BooleanField()
    include_weekly_report = models.BooleanField()
    content_type = models.PositiveSmallIntegerField(choices=ContentType.choices)


class Section(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="sections"
    )
    name = models.CharField(max_length=255)
    draft = models.BooleanField()
    icon_url = models.URLField(null=True)
    small_url = models.URLField(null=True)
    thumb_url = models.URLField(null=True)
    icon_content_type = models.CharField(max_length=255, null=True)
