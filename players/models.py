from django.db import models

class Player(models.Model):
    nickname = models.CharField(max_length=50, unique=True)
    country = models.CharField(max_length=50)
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nickname

    def recalc_rating(self):
        total = self.scores.aggregate(total=models.Sum('points'))['total'] or 0
        self.rating = total
        self.save(update_fields=['rating'])
