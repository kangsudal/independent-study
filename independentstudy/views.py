from django.shortcuts import render

# Create your views here.
def book_list(request):
    return render(request, 'independentstudy/book_list.html', {})