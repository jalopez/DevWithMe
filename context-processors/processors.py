from publication.forms import SnippetForm
from user_profile.forms import RelationshipForm


def pub_form(request):
    pub_form = SnippetForm()
    return {'pub_form': pub_form}

def relationship_form(request):
    relationship_form = RelationshipForm()
    return {'relationship_form': relationship_form}

def relationships(request):
    if request.user.is_authenticated():
        return {'relationships': request.user.get_profile().relationships.all().order_by("user__username")}
    else:
        return {'relationships': None}