from django.db import models

# Create your models here.

class Tags(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Favorite_artist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length = 100)
    artist = models.CharField(max_length = 100)
    
        
class Song(models.Model):
    title = models.CharField(max_length = 100)
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    tags = models.ManyToManyField(Tags)
    favorite_artist = models.OneToOneField(Favorite_artist,on_delete= models.CASCADE)
        
	
    # pub_date = models.DateTimeField(auto_now_add=True)
    # image = models.ImageField(upload_to = 'articles/',blank=True)

