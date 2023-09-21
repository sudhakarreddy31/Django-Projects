from django.shortcuts import get_object_or_404, redirect, render
from abstractmethodsapp.forms import PostForm
from abstractmethodsapp.models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request,'abstractmethodsapp/post_lists.html',{'posts':posts})

def post_detail(request):
    post = get_object_or_404(Post, id='id')
    return render(request, 'abstractmethodsapp/post_details.html', {'post': post})


def post_create(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/lists/")
    return render(request, 'abstractmethodsapp/post_create.html',{'form':form})




def post_update(request,id):
    post = Post.objects.get(id=id)
    form = PostForm(instance=post)
    if request.method =='POST':
        form = PostForm(request.POST,instance='post')
        if form.is_valid():
            form.save()
            return redirect('/lists')
    return render(request, 'abstractmethodsapp/post_update.html', {'form': form})



def post_delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect("/lists")







































































