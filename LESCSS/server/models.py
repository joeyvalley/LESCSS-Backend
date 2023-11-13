from django.db import models


class Meeting(models.Model):
    meeting_title = models.CharField(max_length=200)
    meeting_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    MEETING_TYPES = [
        ("general", "Public"),
        ("lecture", "Lecture"),
        ("conference", "Conference"),
        ("workshop", "Workshop"),
    ]
    meeting_type = models.CharField(max_length=10, choices=MEETING_TYPES)
    meeting_location = models.CharField(max_length=200)
    meeting_guest = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.meeting_title

    def is_lecture(self):
        return self.meeting_type == "lecture"

    def is_conference(self):
        return self.meeting_type == "conference"

    def is_workshop(self):
        return self.meeting_type == "workshop"


class MeetingImage(models.Model):
    meeting = models.ForeignKey(
        Meeting, related_name="images", on_delete=models.CASCADE
    )
    image_url = models.URLField()

    def __str__(self):
        return f"Image for meeting: {self.meeting.meeting_title}"
