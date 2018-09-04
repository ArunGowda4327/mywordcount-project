from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def count(request):
    fulltext = request.GET['fulltext']
    countingwords = fulltext.split()
    mydict = {}
    for word in countingwords:
        if word in mydict:
            mydict[word] += 1
        else:
            mydict[word] = 1



    return render(request, 'count.html', {'fulltext':fulltext,
                  'countingwords':len(countingwords), 'mydict':sorted(mydict.items())})
