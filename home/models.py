from django.db import models

class Duration(models.Model):
    duration = models.CharField(max_length=50)


    def __str__(self):
        return self.duration


class Agent(models.Model):
    # choices is normally a list with tuple element inside
    PROVIDER_CHOICES = [
        ('NZ BEST', 'NZ Best Tour Company'),
        ('NZ First', 'New Zealand First'),
        ('Little Black Bus', 'Little Black Individual Tours')
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    agent_username = models.CharField(max_length=30)
    email_address = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    provider = models.CharField(choices=PROVIDER_CHOICES, max_length=30)

    def __str__(self):
        return self.first_name + ' - ' + self.last_name + ' - ' + self.provider


class Tour(models.Model):
    tour_name = models.CharField(max_length=150)

    """
    'duration' will set to be null when the referenced object (Duration) 
    is deleted. This is only possible when you set 'null' to be 'True'
    """
    duration = models.ForeignKey(Duration, on_delete=models.SET_NULL, null=True)

    description = models.TextField()
    available = models.BooleanField()

    # having similar meaning as duration
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True)

    # Model metadata is “anything that’s not a field”,
    class Meta:
        permissions = (("can_change_availability", "Set tour as available"),)

    # A Python “magic method” that returns a string representation of any object.
    def __str__(self):
        return self.tour_name + ' - ' + self.duration.duration
