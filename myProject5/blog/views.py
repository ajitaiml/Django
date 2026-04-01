from django.shortcuts import render
from datetime import datetime

class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
def home(request):
    context = {
        "name" : "Ajit Singh",
        "age" : "22",
        "skills" : ['python','django','react'],
        "user" : User("Singh",22),
        "blog" : {
            "title" : "Django Template Intro",
            "author" : {
                "name" : "Ajit Singh",
            },
            "content" : "<b>This is Bold</b>",
            "created_at" : datetime(2025,8,18,10,30)
        },
        "empty_value" : None,
    }
    return render(request,"blog/home.html",context)