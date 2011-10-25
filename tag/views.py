from annoying.decorators import render_to

from publication.models import Publication
from models import Tag

@render_to('feed.html')
def tag_feed(request, tag):
    tag_model = Tag.objects.get(tag=tag)
    return {'feed': tag_model.get_feed(), 'tag_feed': tag}