from django.shortcuts import render
from articles.models import Blog
from django.contrib.auth.decorators import login_required
# Create your views here.

def home (request):
    """
    Welcome home page for our fintech application.
    frontend -- 
    """
    all_post = Blog.objects.all()


    context = {
        'all_post':all_post,
    }
    return render(request, 'pages/index.html', context)


def contactus_page (request):
    """
    This is the contact us page for our fintech application.
    """
    
    return render(request, 'pages/contactus.html')
    

@login_required()
def welcome (request):
    """
    This is the contact us page for our fintech application.
    """
    
    return render(request, 'users_pages/index.html')
    