from django.db   import models

from core.models import TimeStampModel

class Category(TimeStampModel):
    name = models.CharField(max_length = 50)
    
    class Meta:
        db_table = 'categories'

class Badge(TimeStampModel):
    name = models.CharField(max_length = 50)
    
    class Meta:
        db_table = 'badges'

class Tag(TimeStampModel):
    type = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100)
    
    class Meta:
        db_table = 'tags'

class Menu(TimeStampModel):
    category    = models.ForeignKey(Category, on_delete = models.CASCADE)
    badge       = models.ForeignKey(Badge, on_delete = models.CASCADE)
    tags        = models.ManyToManyField(Tag, related_name = 'menus')
    name        = models.CharField(max_length = 50)
    description = models.TextField()
    is_sold     = models.BooleanField(default = False)
    deleted_at  = models.DateTimeField(null = True, default = None)
    
    class Meta:
        db_table = 'menus'

class Size(TimeStampModel):
    english_name = models.CharField(max_length = 50)
    korean_name  = models.CharField(max_length = 50)
    
    class Meta:
        db_table = 'sizes'

class Item(TimeStampModel):
    size       = models.ForeignKey(Size, on_delete = models.CASCADE)
    menu       = models.ForeignKey(Menu, on_delete = models.CASCADE)
    price      = models.PositiveIntegerField()
    is_sold    = models.BooleanField(default = False)
    deleted_at = models.DateTimeField(null = True, default = None)
    
    class Meta:
        db_table = 'items'

