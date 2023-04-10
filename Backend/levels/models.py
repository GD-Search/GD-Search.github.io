from django.db import models

# Create your models here.
class Level(models.Model):
    level_name = models.CharField(max_length=100)
    creator_id = models.ForeignKey('Player', on_delete = models.CASCADE)
    level_id = models.IntegerField()
    gd_version = models.CharField(max_length=5)
    rating = models.CharField(max_length=20)
    is_collab = models.BooleanField()
    duration = models.CharField(max_length=20)
    objects_type = models.Field()

    def __str__(self) -> str:
        return self.level_name

class Player(models.Model):
    player_name = models.CharField(max_length=20)
    player_description = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.player_name

class CollabMembers(models.Model):
    level_id = models.ForeignKey('Level', on_delete=models.CASCADE)
    creator_id = models.ManyToManyField('Player')

    def __str__(self) -> str:
        return f"{self.level_id} {self.creator_id}"