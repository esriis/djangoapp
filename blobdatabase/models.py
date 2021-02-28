from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.name 
    
class Project(models.Model):
    name = models.CharField(max_length=100)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    class Meta:
        unique_together = ('name', 'client',)
    def __str__(self):
        return self.name 
    
    
class SubProject(models.Model):
    dataType = models.CharField(max_length=100)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    class Meta:
        unique_together = ('dataType', 'project')
    def __str__(self):
        return self.project.name + ", " + self.dataType 
    

class Blob(models.Model):
    name = models.CharField(max_length=200)
    fullPath = models.CharField(max_length=400,unique=True)
    subProject = models.ForeignKey(SubProject,on_delete=models.CASCADE)
    modifiedDate = models.DateTimeField('date modified')
    # createdDate = models.DateTimeField('date created')
    modifiedBy = models.CharField(max_length=100)
    # createdBy = models.CharField(max_length=100)
    guid = models.CharField(max_length=50,unique=True)
    extension = models.CharField(max_length=30)
    class Meta:
        ordering = ['guid']
    def __str__(self):
        return self.fullPath
