from django.shortcuts import get_object_or_404, redirect
from annoying.decorators import render_to
from django.http import HttpResponseForbidden
from models import Publication, Comment, Snippet
from forms import ReplyForm, SnippetForm

from tag.models import Tag

@render_to('publication.html')
def publication_detail(request, pub_id):
    pub = get_object_or_404(Publication, pk=pub_id)
    if pub.reply_to_pub != None:
        return HttpResponseForbidden("This is a response, access to the parent to see its details")
    replies = Publication.objects.filter(reply_to_pub=pub).order_by("date")
    return {'pub': pub, 'replies': replies, 'comment_form': ReplyForm()}

def add_publication(request):
    if request.method != 'POST':
        return HttpResponseForbidden("Method not allowed")
    
    next = "/"
    if (request.GET.has_key("next")):
        next = request.GET["next"]
        
    reply_to = None
    if request.POST.has_key("reply_to"):
        reply_to = request.POST["reply_to"]
        
    if reply_to:
        form = ReplyForm(request.POST)
        pub = create_comment(request, form, reply_to)
    else:
        form = SnippetForm(request.POST)
        pub = create_snippet(request, form)
    
    if (pub):
        return redirect(next)
    else:
        #add error
        return redirect(next)
        
def create_comment(request, form, reply_to):
    if not form.is_valid():
        return None
    
    text = form.cleaned_data['text']
    title = form.cleaned_data['title']
    
    comment = Comment(title=title, text=text)
    comment.save()    
    reply_pub = Publication.objects.get(pk=reply_to)
    
    pub = Publication(content=comment, reply_to_pub=reply_pub, is_public=True, published_by=request.user.get_profile())
    pub.save()
    return pub 
    

def create_snippet(request, form):
    if not form.is_valid():
        return None
    
    text = form.cleaned_data['text']
    title = form.cleaned_data['title']
    is_public = form.cleaned_data['is_public']
    
    snippet = Snippet(title=title, text=text)
    snippet.save()
    add_tags(snippet, form.cleaned_data['tags'])
    pub = Publication(content=snippet, reply_to_pub=None, is_public=is_public, published_by=request.user.get_profile())
    pub.save()
    
    return pub

def add_tags(content, tags_string):
    if (tags_string != ""):
        [get_or_create_tag(content, t) for t in tags_string.split(",")]
    
def get_or_create_tag(content, t):
    tag, created = Tag.objects.get_or_create(tag=t)
    if (created):
        tag.save()
        
    content.tags.add(tag)
    
    return tag
    