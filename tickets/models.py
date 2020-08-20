from django.db import models

# Create your models here.

class TeamName(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Engineer(models.Model):
    name = models.CharField(max_length=25)
    plusrid = models.CharField(max_length=15)
    teamname = models.ForeignKey(TeamName,on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Ticket(models.Model):
    ticketno = models.CharField(max_length=20,null=True)
    # teamname = models.ForeignKey(TeamName,on_delete=models.CASCADE,default="",null=True)
    # name = models.OneToOneField(Engineer,on_delete=models.CASCADE,default="",null=True)
    teamname = models.CharField(max_length=20,null=True)
    name = models.CharField(max_length=20,null=True)
    priority = models.CharField(max_length=20,null=True)
    ticketstatus = models.CharField(max_length=20,null=True)
    tktdescription = models.TextField(null=True)
    inccreddate = models.DateTimeField(auto_now_add=False, auto_now=False,null=True)
    increcddate = models.DateTimeField(auto_now_add=False, auto_now=False,null=True)
    incsolddate = models.DateTimeField(auto_now_add=False, auto_now=False,null=True)
    slasatus = models.CharField(max_length=20,null=True)
    slamteam = models.CharField(max_length=20,null=True)
