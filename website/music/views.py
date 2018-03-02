from django.http import HttpResponse

def index(request):
    #page="<input type='text' />" showing error
    return  HttpResponse("<h1>welcome to music app</h1>")
