from django.shortcuts import render
from django.http import HttpResponse
import spacy
from nlpApps.models import Document
from spacy import displacy
from .forms import UploadFileForm
# handle_uploaded_file







nlp = spacy.load("fr_core_news_md")

def home(request):
    return render(request, 'nlpApps/index.html')


def submit_form_ner(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES.get('file')
            if file:
                text = str(file.read(), 'utf-8')
            else:
                text = request.POST['user_input']
            doc = nlp(text)
            if doc.ents:
                html = displacy.render(doc, style="ent")
            else:
                html = "No entities found"
            return render(request, 'nlpApps/ner.html', {'result': html, 'text': text, 'form': form})
    else:
        return render(request, 'nlpApps/ner.html', {'form': UploadFileForm()})
    

