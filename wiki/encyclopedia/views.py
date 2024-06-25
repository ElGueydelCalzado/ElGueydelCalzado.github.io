from django.shortcuts import redirect, render
from . import util
import markdown2

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {
            'message': f"The requested page '{title}' was not found.",
            'title': title  # Pass the title for a more personalized error message
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": content
        })
    
def search(request):
    query = request.GET.get('q')
    if util.get_entry(query):
        return render(request, "encyclopedia/entry.html", {
            "title": query,
            "content": util.get_entry(query)
        })
    else:
        entries = util.list_entries()
        results = [entry for entry in entries if query.lower() in entry.lower()]
        return render(request, "encyclopedia/search.html", {
            "results": results
        })

def new_page(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        if util.get_entry(title) is not None:
            return render(request, "encyclopedia/error.html", {
                "title": title
            })
        else:
            util.save_entry(title, content)
            return redirect('encyclopedia:entry', title=title)
    
    return render(request, "encyclopedia/new_page.html")
