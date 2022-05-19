from django.shortcuts import render, redirect
from PyDictionary import PyDictionary

# Create your views here.
def index(request):
    return render(request, 'index.html')

def word(request):
    search = request.GET.get('search')
    dictionary = PyDictionary()
    meaning = dictionary.meaning(search)
    synonyms = dictionary.synonym(search)
    antonyms = dictionary.antonym(search)

    print(synonyms)
    print(antonyms)
    
    if synonyms == None and antonyms == None:
        context = {
            'meaning': meaning,
            'synonyms': ['No synonym found'],
            'antonyms': ['No antonym found'],
        }
    else:

        context = {
            'meaning': meaning,
            'synonyms': synonyms,
            'antonyms': antonyms,
        }

    return render(request, 'word.html', context)