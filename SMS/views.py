from django.http import HttpResponse

#HttpResponse is used to display the message on browser
def home(request):
    return HttpResponse("First Django Project")

def admin(request):
    return HttpResponse("I am in Admin Page")
def user(request):
    return HttpResponse("<b>I am in User Page</b>")

def display(request):
    name="KLU"
    output = "My Name is ",name
    return HttpResponse(output)