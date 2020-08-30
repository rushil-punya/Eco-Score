from django.db import models

#this model allows the data for each individual cell in the ecoscore
#app to be stored in the database and recalled later during calculation
class Cell(models.Model):
    title = models.CharField(max_length=100)
    numPoints = models.IntegerField()
    slug = models.SlugField(default="s")
    isClean = models.BooleanField(default=False)
    isSelected = models.BooleanField(default=False)


    def __str__(self):
        return self.title
