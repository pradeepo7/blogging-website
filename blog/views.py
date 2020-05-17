from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import ListView , DetailView, CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# from django.core.paginator import Paginator
#       "title":"bsc program",
#       'content':"senti",
#       'date_posted':'18 feb 2000'

#      },
     
#      {"author":"divya",
#       "title":"mcom",
#       'content':"organzion sector",
#       'date_posted' :'5 may 2001'

#      }
# ]


def home(request):
    context ={
        'post':Post.objects.all()
    }
    return render(request,'blog/home.html',context)   #you can't pass more than one argument


def about(request):
    return render(request,'blog/about.html',{'title':'about '})

class PostListView(ListView):
    model = Post
    template_name ="blog/home.html"
    context_object_name = 'post'
    ordering =  ['-date_posted'] 
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name ="blog/user_posts.html"
    context_object_name = 'post'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

    
class PostdetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']

    def test_func(self):
        post = self.get_object()

        if post.author == self.request.user:
            return True
        return False    

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'


    def test_func(self):
        post = self.get_object()
        

        if post.author == self.request.user:
            return True
        return False    

