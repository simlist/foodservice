# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Category(models):
    name = models.Charfield(maxlength=20)
    slug = models.SlugField(max_length=30)

