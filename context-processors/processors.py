
from publication.forms import SnippetForm, MessageForm
from user_profile.forms import RelationshipForm


def common_forms(request):
    pub_form = SnippetForm()
    relationship_form = RelationshipForm()
    msg_form = MessageForm()
    return {'pub_form': pub_form, 'msg_form': msg_form, 'relationship_form': relationship_form}

def relationships(request):
    if request.user.is_authenticated():
        return {'relationships': request.user.get_profile().relationships.all().order_by("user__username")}
    else:
        return {'relationships': None}
