from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_delete
from django.dispatch import receiver

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=200, null=False)
    content = models.CharField(max_length=200, null=False)
    urgency = models.CharField(max_length=200, null=True)
 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.name
    
    # The absolute path to get the url then reverse into 'student_edit' with keyword arguments (kwargs) primary key
    def get_absolute_url(self):
        return reverse('notes_edit', kwargs={'pk': self.pk})


@receiver(pre_delete,sender=Notes)
def h(sender,instance,**kwargs):
    print(instance.title)
    f = open("debug.log", "a")
    f.write("+")
    f.write(instance.title)
    f.write("++")
    f.close()


    
