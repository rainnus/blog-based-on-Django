from django.shortcuts import render_to_response
from django.http import Http404
from myapp.models import Blog
from myapp.models import Tag
from django.template import RequestContext

# Create your views here.
def blog_list(request):
    Blogs = Blog.objects.all()
    tags = Tag.objects.all()
    return render_to_response("blog_list.html", {"Blogs": Blogs, "tags": tags})

def blog_show(request, id = ''):
    try:
        Blogs = Blog.objects.all()
        blog = Blog.objects.get(id = id)
        tags = Tag.objects.all()
    except Blog.DoesNotExist:
        raise Http404
    return render_to_response("blog_show.html", {"Blogs": Blogs,"Blog":blog,"tags": tags}, context_instance=RequestContext(request))


def blog_show_comment(request, id=''):
    blog = Blog.objects.get(id=id)
    return render_to_response('blog_comments_show.html', {"blog": blog})