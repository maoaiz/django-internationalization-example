from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


def home(request):
    o = _("Hello world I am a translated text").encode("utf-8")
    articles = list()
    articles.append({"title": "Title", "date": "November 1st of 2012", "content": "Content"})
    articles.append({"title": "Other Title", "date": "December 2nd of 2012", "content": "More Content"})
    ctx = {
        "redirect_to": "/",
        "text": o,
        "articles": articles
    }
    return render_to_response("index.html", ctx, context_instance=RequestContext(request))
