import os
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.utils.text import slugify
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Post, Comment
from .form import CommentForm



# Create your views here.
def index(request):
    '''
    장고가 기본적으로 제공하는 render() 함수를 사용행 템플릿 폴더에서 
    blog 폴더의 index.html 파일을 찾아 방문자에게 보낸다.
    
        (1) FBV(Function based view)로 페이지 목록 제작
    '''

    posts = Post.objects.all().order_by('-pk')
    query = request.GET.get('query','')

    page = request.GET.get('page', '1') 

    paginator = Paginator(posts, 5)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    return render(
        request,
        'blog/post_list.html',
        {
            'posts' : page_obj,
            'page' : page,
            'query' : query
        }
    )

def post_page(request, pk):

    post = Post.objects.get(pk=pk)
    comments = Comment.objects.get(pk=pk)
    file_name = os.path.basename(post.file_upload.name) 

    return render(
        request,
        'blog/post_page.html',
        {
            'post' : post,
            'file_name' : file_name,
            'comments' : comments
        }
    )

class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_page.html'
    
    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        # context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        context['comment_form'] = CommentForm
        return context
    
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login 
from django.shortcuts import redirect
from django.http import JsonResponse
from .form import UserForm

@login_required
def write_page(request):
    return render(
        request,  'write.html'
    )

import fitz
@login_required
def write_file(request):
    summary = "..."

    if request.method == "POST":
        uploaded_file = request.FILES.get('file')

        file_name = uploaded_file.name.lower()
        extracted_text = ""
        try:
            if file_name.endswith('.pdf'):
                file_data = uploaded_file.read()
                # PyMuPDF로 PDF 열기 (stream 인자를 사용)
                doc = fitz.open(stream=file_data, filetype="pdf")

                for page in doc:
                    extracted_text += page.get_text()

            elif file_name.endswith('.txt'):
                # 텍스트 파일 읽기: 파일 객체를 읽고, 디코딩 (여기서는 utf-8로 가정)
                text = uploaded_file.read().decode('utf-8')
            else:
                return JsonResponse({'error': '지원하지 않는 파일 형식입니다.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': f'파일 읽기 중 오류 발생: {str(e)}'}, status=500)

        summary = summarize_text_with_openai(extracted_text)

    return JsonResponse(
        {
            'message':'ok', 
            'summary_text' : summary
        },
        status=200
    )

@login_required
def write_post(request):
    if request.method == "POST":
        user = User.objects.get(id=request.user.id)

        post = Post(
            title = request.POST.get('bdTitle'),
            content=request.POST.get('bdContent'),
            file_upload=request.FILES.get('bdFile'),
            summarize_content=request.POST.get('bdContent'),
            author=user
        )

        post.save()

        return redirect('/blog')

def login_page(request):
    return render(
        request,  'login.html'
    )

def signup_page(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserForm()
    return render(
        request, 
        'signup.html', 
        {
            'form' : form,
        }
    )

# OpenAI를 사용하여 텍스트 요약 함수
import os
import environ
import requests
import openai
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)
openai.api_key = env('OPENAI_API_KEY')

def summarize_text_with_openai(text, max_tokens=150):
    """OpenAI API를 사용해 텍스트를 요약하는 함수: 환경문제로 FastAPI 붙였어요.
    
    uvicorn summarize:app --reload --host 0.0.0.0 --port 18000
    """
    
    summary = "..."

    url = "http://127.0.0.1:18000/summarize/"
    data = {
        "text": text
    }

    response = requests.post(url, json=data)

    # 응답을 확인합니다.
    if response.status_code == 200:
        summary = response.json()['summary']
    else:
        summary = f"요청 실패: {response.status_code}" + summary

    return summary  