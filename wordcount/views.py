from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html')


def count(request):
    fullText = request.GET['fullText']
    wordList = fullText.split()

    wordDictionary = {}

    for word in wordList:
        if word in wordDictionary:
            wordDictionary[word] += 1
        else:
            wordDictionary[word] = 1

    sortedWords = sorted(wordDictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fullText': fullText, 'count': len(wordList),'wordDictionary': sortedWords })

def about(request):
    return render(request, 'about.html')