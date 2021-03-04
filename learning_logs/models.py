from django.db import models

class Topic(models.Model):
    """The subject the user is studing."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns str type model."""
        return self.text

class Entry(models.Model):
    """Information studing by the user on the topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Output string representation model."""
        if len(self.text) > 50:
            return f'{self.text[:50]}...'
        else:
            return self.text
