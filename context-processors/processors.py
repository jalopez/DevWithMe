from publication.forms import SnippetForm

def pub_form(request):
    pub_form = SnippetForm()
    return {'pub_form': pub_form}