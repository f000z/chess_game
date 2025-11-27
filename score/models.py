from django.db import models
from django.core.exceptions import ValidationError
from game.models import Game
from players.models import Player

RESULT_CHOICES = (
    ('win', 'Win'),
    ('draw', 'Draw'),
    ('loss', 'Loss'),
)

POINTS_MAP = {
    'win': 10,
    'draw': 5,
    'loss': 0
}

class Score(models.Model):
    game = models.ForeignKey(Game, on_delete=models.PROTECT)
    player = models.ForeignKey(Player, related_name='scores', on_delete=models.PROTECT)
    result = models.CharField(max_length=10, choices=RESULT_CHOICES)
    points = models.IntegerField()
    opponent_name = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def clean(self):
        if self.result not in POINTS_MAP:
            raise ValidationError("Invalid result. Must be 'win', 'draw' or 'loss'.")

    def save(self, *args, **kwargs):
        self.points = POINTS_MAP.get(self.result, 0)
        super().save(*args, **kwargs)
