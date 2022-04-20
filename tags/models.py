from django.db import models

import tags


class Tag(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)
    deadline_time = models.DateTimeField(blank=True, null=True)
    is_done = models.BooleanField(default=False)
    tag = models.ManyToManyField(Tag, related_name="tags")

    class Meta:
        ordering = ["is_done", "create_time"]

    def __str__(self):
        return f"{self.content} - {self.is_done}/n" \
               f" Created: {self.create_time}. Deadline: {self.deadline_time}./n" \
               f"Tags: {self.tag}"


