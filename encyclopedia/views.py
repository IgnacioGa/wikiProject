from django.shortcuts import render
import random
from . import util
from django.contrib import messages
import markdown2
from django.utils.safestring import mark_safe


def buscar(x):
	listSubEntry = []
	entries = util.list_entries()
	for entry in entries:		
		if x in entry:
			listSubEntry.append(entry)
	return listSubEntry

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request, entry):
	if (util.get_entry(entry)!=None):
		return render(request, "encyclopedia/page.html", {
        "entry": entry.capitalize(),
        "content": markdown2.markdown(util.get_entry(entry))
        	})       	      
	else:
		return render(request, "encyclopedia/error.html")

def search(request):
	entry = request.GET.get('q')
	print(entry)	
	if(util.get_entry(entry)!=None):
		return render(request, "encyclopedia/page.html", {
        "entry": entry.capitalize(),
        "content": markdown2.markdown(util.get_entry(entry))
        	})
	else:
		lista = buscar(entry)
		return render(request, "encyclopedia/search.html", {
		"entry": entry,
        "result": lista
        	})

def Rpage(request):
	entries = util.list_entries()
	page = random.choice(entries)
	return render(request, "encyclopedia/page.html", {
        "entry": page.capitalize(),
        "content": markdown2.markdown(util.get_entry(page))
        	}) 

def create(request):
	entries = util.list_entries()
	if request.method == "POST":
		entry = request.POST["title"]
		content = request.POST["content"]	
		if entry in entries:
			messages.error(request, mark_safe("This entry already exists. <a href='/wiki/"+entry+"'>"+entry+" entry </a>"))
			return render(request, "encyclopedia/create.html",{
	   			"entry": entry,
	   		    "content": content
	   				})
		else:
			util.save_entry(entry, content)
			return render(request, "encyclopedia/page.html", {
        		"entry": entry.capitalize(),
        		"content": markdown2.markdown(util.get_entry(entry))
        			}) 
	else:
		return render(request, "encyclopedia/create.html")

def edit(request, entry):
	if request.method == "POST":
		text = request.POST["editable"]
		util.save_entry(entry, text)
		return render(request, "encyclopedia/page.html", {
        		"entry": entry.capitalize(),
        		"content": markdown2.markdown(util.get_entry(entry))
        			})
	else:
		return render(request, "encyclopedia/edit.html",{
			"entry": entry.capitalize(),
        	"txtedit": util.get_entry(entry)
				})