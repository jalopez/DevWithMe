from django.shortcuts import get_object_or_404
from annoying.decorators import render_to
from django.http import HttpResponseForbidden
from models import Publication
from forms import ReplyForm

@render_to('publication.html')
def publication_detail(self, pub_id):
    pub = get_object_or_404(Publication, pk=pub_id)
    if pub.reply_to_pub != None:
        return HttpResponseForbidden("This is a response, access to the parent to see its details")
    replies = Publication.objects.filter(reply_to_pub=pub).order_by("date")
    return {'pub': pub, 'replies': replies, 'pub_form': ReplyForm()}