from django.shortcuts import render, get_object_or_404
from blog.models import Post
# Create your views here.

def search_page(request):
    posts = Post.objects.all().order_by('-pk')
    query = request.GET.get('query','')
    print(query)



    return render(
        request,
        'blog/index.html',
        {
            'posts' : posts,
        }
    )