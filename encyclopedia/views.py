from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request, entry):
	if (util.get_entry(entry)!=None):
		return render(request, "encyclopedia/page.html", {
        "entry": entry.capitalize(),
        "content": util.get_entry(entry)
        	})      
	else:
		return HttpResponseRedirect(reverse("index"))
