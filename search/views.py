from django.shortcuts import render, get_object_or_404, redirect 
from blog.models import Post
from .forms import UserForm
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
import openai  # OpenAI API 라이브러리
import fitz  # PyMuPDF
from django.contrib.auth.models import User
from django.conf import settings


# OpenAI API 키 설정
openai.api_key = settings.OPENAPI_KEY
# Create your views here.

def search_page(request):
    posts = Post.objects.all().order_by('-pk')
    query = request.GET.get('query','')

    page = request.GET.get('page', '1') 

    paginator = Paginator(posts, 10)  # 페이지당 10개씩 보여주기
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
@login_required
def write_page(request):
    return render(
        request,  'write.html'
    )

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
    return render(request, 'signup.html', {'form' : form })

@login_required
def write_file(request):
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

        return JsonResponse({'message':'ok', 'summary_text' : summary}, status=200)

@login_required
def write_post(request):
    if request.method == "POST":
        user = User.objects.get(id=request.user.id)

        post = Post(
            title = request.POST.get('bdTitle'),
            content=request.POST.get('bdContent'),
            file_upload=request.FILES.get('bdFile'),
            user=user
        )

        post.save()

        return redirect('/')

# OpenAI를 사용하여 텍스트 요약 함수
def summarize_text_with_openai(text, max_tokens=150):
    """OpenAI API를 사용해 텍스트를 요약하는 함수"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # 최신 GPT-3.5-turbo 모델 사용
        messages=[  
            {"role": "system", "content": "너는 문서의 텍스트를 받아서 요약해주는 역할을 해야돼."},   # You are a helpful assistant.
            {"role": "user", "content": f"다음 텍스트를 3문장으로 요약해 주세요:\n\n{text}"}  ,
            {"role": "user", "content": """ 형식은 아래를 참고해서 작성해줘.
                문서 제목 
               - 문장1
               - 문장2
               - 문장3
            """}  
        ],
        max_tokens=max_tokens,  
        temperature=0.7  
    )
    
    summary = response['choices'][0]['message']['content'].strip()  # 요약된 텍스트 반환
    return summary  