from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import markdown
from .models import MarkdownContent


def apiauto(request, md_content):
        
    # set the extension for markdown
    md = markdown.Markdown(extensions=["fenced_code","codehilite"])        
    # read the md content according to title
    markdown_content = MarkdownContent.objects.get(title=md_content)    
    markdown_content.content = md.convert(markdown_content.content)
    context = {
        "markdown_content": markdown_content
    }
    template = loader.get_template('api_auto.html')
    
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def all(request):
    template = loader.get_template('all.html')
    return HttpResponse(template.render())

def markdown_content_view(request, md_content):
    md = markdown.Markdown(extensions=["fenced_code","codehilite"])
    # markdown_content = MarkdownContent.objects.first()
    # markdown_content = MarkdownContent.objects.get(id=2)
    print(md_content)
    markdown_content = MarkdownContent.objects.get(title=md_content)
    print(markdown_content)
    markdown_content.content = md.convert(markdown_content.content)
    context = {
        "markdown_content": markdown_content
    }
    template = loader.get_template('markdown_content.html')
    
    return HttpResponse(template.render(context, request))
    # return render(
    #     request,
    #     "markdown_content.html",
    #     context=context
    # )
