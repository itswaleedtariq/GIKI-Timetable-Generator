from django.db import models

class TimetableEntry(models.Model):
    course_name = models.CharField(max_length=100)
    teacher_name = models.CharField(max_length=100)
    classroom_name = models.CharField(max_length=50)
    section_name = models.CharField(max_length=50)
    day = models.CharField(max_length=20)
    start_time = models.CharField(max_length=10)
    end_time = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.course_name} - {self.section_name}"