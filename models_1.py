from django.db import models
from django.contrib.auth.models import User


class Player(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_login = models.DateTimeField(auto_now_add=True)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class Boost(models.Model):
    BOOST_TYPE_CHOICES = [
        ('exp', 'EXP'),
        ('hp', 'HP'),
        ('shield', 'SHIELD'),
        ('speed', 'SPEED'),
        # Добавить нужное
    ]

    id = models.AutoField(primary_key=True)
    boost_type = models.CharField(max_length=10, choices=BOOST_TYPE_CHOICES)
    boost_value = models.IntegerField()
    description = models.TextField(max_length=1000)


class PlayerBoost(models.Model):
    id = models.AutoField(primary_key=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    boost = models.ForeignKey(Boost, on_delete=models.CASCADE)
    received = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.player.user.username} - {self.boost.boost_type}'

