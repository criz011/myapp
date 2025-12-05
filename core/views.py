from django.http import HttpResponse

def home(request):
    return HttpResponse("Todo API is running. Use /todo/ endpoints.")
