from django.db import models  
class Scores(models.Model):  #Model for inputs in database
    
    Player_name = models.CharField(max_length=50)  
    Score = models.BigIntegerField()   
    class Meta:  
        db_table = "scores"  