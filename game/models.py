# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Game(models.Model):
    id = models.BigAutoField(primary_key=True)  #
    board = models.CharField(max_length=9, default=' ' * 9)
    current_player = models.CharField(max_length=1, default='X')
    winner = models.CharField(max_length=1, null=True, blank=True)
    game_over = models.BooleanField(default=False)

    def __str__(self):
        return self.board
