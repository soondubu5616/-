from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone

# Create your views here.
def home(request):
    blogs = Blog.objects #쿼리셋
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details': details})#리퀘스트가 들어오면 html에 딕셔너리를 입력하여 띄운다

def new(request): #new.html 띄워주는 함수
    return render(request, 'new.html') #리퀘스트가 들어오면 html을 띄운다

def create(request): #입력받은 내용을 db에 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))
    