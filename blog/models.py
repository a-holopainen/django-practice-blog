from django.db import models
from django.utils import timezone
import datetime


class Problem(models.Model):

    AVAILABLE_STATUS = 1
    UNDER_CONSTRUCTION_STATUS = 2
    TAKEN_DOWN_STATUS = 3
    STATUS_CHOICES = (
        (AVAILABLE_STATUS, 'Available'),
        (UNDER_CONSTRUCTION_STATUS, 'Under construction'),
        (TAKEN_DOWN_STATUS, 'Taken down'),
    )

    TWO_HOLD_START = 1
    ONE_HOLD_START = 2
    OTHER_START = 3
    START_CHOICES = (
        (TWO_HOLD_START, 'Start has 2 holds'),
        (ONE_HOLD_START, 'Start has 1 hold'),
        (OTHER_START, 'Exceptional start - instructions on the wall'),
    )

    LAST_HOLD_END = 1
    TOP_EDGE_END = 2
    OTHER_END = 3
    END_CHOICES = (
        (LAST_HOLD_END, 'Last hold is marked'),
        (TOP_EDGE_END, 'Problem ends at top edge'),
        (OTHER_END, 'Special ending - instructions on the wall'),
    )

    GREEN_GRADE = 1
    BLUE_GRADE = 2
    RED_GRADE = 3
    BLACK_GRADE = 4
    WHITE_GRADE = 5
    GREY_GRADE = 6
    GRADE_CHOICES = (
        (GREEN_GRADE, 'Green'),
        (BLUE_GRADE, 'Blue'),
        (RED_GRADE, 'Red'),
        (BLACK_GRADE, 'Black'),
        (WHITE_GRADE, 'White'),
        (GREY_GRADE, 'Grey'),
    )

    builder = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=AVAILABLE_STATUS)
    start_type = models.IntegerField(choices=START_CHOICES, default=TWO_HOLD_START)
    end_type = models.IntegerField(choices=END_CHOICES, default=LAST_HOLD_END)
    grade = models.IntegerField(choices=GRADE_CHOICES, default=BLUE_GRADE)
    grip_color = models.CharField(max_length=200, default='color not defined')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    expected_expiry_date = models.DateTimeField(default=datetime.datetime.now() + datetime.timedelta(days=35))
    actual_expiry_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
