from django.shortcuts import render
from django.http import HttpResponse
import spacy
from spacy import displacy
nlp = spacy.load("fr_core_news_md")

def home(request):
    return render(request, 'nlpApps/ner.html')


def submit_form_ner(request):
    if request.method == 'POST':
        text = request.POST['user_input']
        doc = nlp(text)
        html = displacy.render(doc, style="ent")
        return HttpResponse(html)
    else:
        return HttpResponse('Invalid request')
