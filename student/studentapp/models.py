from django.db import models

# Create your models here.

class studentmarks(models.Model):
    rollno = models.IntegerField()
    name = models.CharField(max_length=50)
    mark1 = models.IntegerField()
    mark2 = models.IntegerField()
    mark3 = models.IntegerField()
    mark4 = models.IntegerField(default=False)
    mark5 = models.IntegerField(default=False)

class Meta:
    
    db_table = 'student_marks'
    unique_together = ['rollno']

def _str_(self):
    return self.rollno,self.name,self.mark1,self.mark2,self.mark3,self.mark4,self.mark5
    
