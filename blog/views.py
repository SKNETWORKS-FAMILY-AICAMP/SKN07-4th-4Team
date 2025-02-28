import os

from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    '''
    장고가 기본적으로 제공하는 render() 함수를 사용행 템플릿 폴더에서 
    blog 폴더의 index.html 파일을 찾아 방문자에게 보낸다.
    
        (1) FBV(Function based view)로 페이지 목록 제작
    '''
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'blog/post_list.html',
        {
            'posts' : posts,
        }
    )

def post_page(request, pk):

    post =  Post.objects.get(pk=pk)
    file_name = os.path.basename(post.file_upload.name) 

    return render(
        request,
        'blog/post_page.html',
        {
            'post' : post,
            'file_name' : file_name
        }
    )