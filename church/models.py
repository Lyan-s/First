from django.db import models

# Create your models here.
class ChurchDetails(models.Model):
    church_name = models.CharField(max_length=100)
    welcome_line = models.CharField(
        max_length = 200,
        help_text = "The greeting shown at the top of the Home page"
    )
    theme_of_the_year = models.CharField(max_length=100)
    address = models.CharField(
        max_length=200,
        help_text= "Your location"
    )
    service_times = models.TextField(help_text="Write one service per line E.g Sunday 10:00 a.m - main service")
    email = models.EmailField(help_text = "Your Email")

    def __str__(self):
        return self.church_name
    class Meta:
        verbose_name_plural = "Church Details"



class Announcements(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField(
        blank=True,
        help_text="Write the announcements here.",
        )
    date_posted = models.DateField(auto_now_add=True)
    show_until = models.DateField(
        blank=True,
        null=True,
        help_text="Optional , The announcement stops showing after this date. ",
    )


    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Announcements"

class Leader(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(
        max_length=50,
        help_text="For example ; Pastor,Elder"
    )
    photo = models.ImageField(
        upload_to="leaders/",
        blank=True,
        )
    order = models.PositiveIntegerField(
        default=0,
        help_text="Smaller numbers are shown first."
    )
    currently_serving = models.BooleanField(
        default=True,
        help_text="Untick this when the person leaves the role.",
    )

    def __str__(self):
        return self.name