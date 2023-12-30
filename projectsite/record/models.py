from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class artist(BaseModel):
    artistID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Email = models.EmailField()
    ProfileImage = models.ImageField(upload_to='artist_images/',blank=True, null=True)

    def __str__(self):
        return f"{self.ProfileImage} {self.FirstName} {self.LastName}"

class duration(BaseModel):
    durationID = models.AutoField(primary_key=True)
    durationName = models.CharField(max_length=255)
    artistID = models.ForeignKey(artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.durationName

class title(BaseModel):
    SongNameID = models.AutoField(primary_key=True)
    Artist = models.CharField(max_length=255)
    Duration = models.CharField(max_length=255)
  
    def __str__(self):
        return f"{self.SongNameID} {self.Artist}"

class albums(BaseModel):
    titleID = models.ForeignKey(title, on_delete=models.CASCADE)
    durationID = models.ForeignKey(duration, on_delete=models.CASCADE)

class date_added(BaseModel):
    date_addedID = models.AutoField(primary_key=True)
    Song_Added = models.CharField(max_length=255, default="YourDefaultValueHere")
    durationID = models.ForeignKey(duration, on_delete=models.CASCADE)
    date_addedName = models.CharField(max_length=255)

    def __str__(self):
        return self.date_addedName



