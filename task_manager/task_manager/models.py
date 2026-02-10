from django.db import models

class TaskList(models.Model):
    id =models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    


class Task(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    task_list=models.ForeignKey(TaskList,on_delete=models.CASCADE)

    def __str__(self):
        return self.title