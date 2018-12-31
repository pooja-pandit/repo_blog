from django.shortcuts import render,HttpResponse,redirect,Http404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from blog.models import Blog,Category,Topic,Comment
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from rest_framework.permissions import AllowAny
from blog.serializers import BlogSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser





class GenericBlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('category','topics','author')
    pagination_class = PageNumberPagination

class GenericBlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (AllowAny,)

@csrf_exempt
def blog_list_api(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BlogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def blog_detail_api(request,blog_id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        blog = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BlogSerializer(blog)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BlogSerializer(blog, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        blog.delete()
        return HttpResponse(status=204)

def about(request):
    contextlist={'name':'pooja','company':'livewire','l':(1,2,3,4,5)}

    return render(request,'about.html',contextlist)

def category_list(request):
    categories=Category.objects.all()

    return render(request,'category_list.html',{'categories':categories})


def category_detail(request,category_id):
    blogs_filtered = Blog.objects.filter(category = category_id)
    paginator = Paginator(blogs_filtered, 2)  # Show 25 contacts per page

    page = request.GET.get('page')
    category_list = paginator.get_page(page)
    return render(request, 'categorydetail.html', {'category_list':category_list})

def contact(request):
    return HttpResponse("contact Us")

def write_comment(request):
    if request.method=='POST':
        comment=request.POST['text']
        c=Comment(text=comment)
        c.save()
    return render(request,'comment.html',{})

@login_required
def approve_comment(request,comment_id):
    comment=Comment.objects.get(id=comment_id)
    comment.approve()
    return redirect('blogdetail',blog_id=comment.blogs.id)

@login_required
def remove_comment(request,comment_id):
    comment=Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('blogdetail',blog_id=comment.blogs.id)




def blog_list(request):
    blogs=Blog.objects.all()
    topics=Topic.objects.all()
    paginator = Paginator(blogs, 2)  # Show 25 contacts per page

    page = request.GET.get('page')
    blog_list = paginator.get_page(page)
    return render(request,"blog_list.html",{'blog_list':blog_list,'topics':topics})

def topic_list(request,topic_id):
    topic = Topic.objects.get(id=topic_id)
    # blogs= topic.blog_set.all()
    blogs = Blog.objects.filter(topics=topic_id)
    return render(request, "topic_list.html", {'blogs':blogs})

def blog_detail(request,blog_id):
    blog=Blog.objects.get(id=blog_id)
    comments = Comment.objects.filter(blogs = blog_id)
    if request.method == 'POST':
        comment = request.POST['text']
        user = request.user
        c = Comment(text=comment, author=user, blogs=blog)
        c.save()
    return render(request, "blog_detail.html", {'blog': blog, 'comments':comments})
def home(request):
    return HttpResponse("home")
# Create your views here.

def add_new_blog(request):
    context_dict={'submitted':False}
    if request.method=='POST':
        h=request.POST['header']
        s = request.POST['subheader']
        d = request.POST.get('details',False)
        b=Blog(header=h,subheader=s,details=d)
        b.save()
        context_dict['submitted']=True
        #return HttpResponse('fg ghgh')
    return render(request,'add_blog.html',context_dict)
