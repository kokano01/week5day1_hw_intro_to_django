from django.shortcuts import render
# Create your views here.
def index(request):
    my_top5 = [
        {
            'title' : 'Moratorium',
            'artist' : 'Omoinotake',
            'year' : '2020'
        },
        {
            'title' : 'Fourth of July',
            'artist' : 'Fall Out Boys',
            'year' : '2015'
        },
        {
            'title' : 'Window',
            'artist' : 'Joji',
            'year' : '2017'
        },
        {
            'title' : 'Sadderday',
            'artist' : 'tobi lou',
            'year' : '2018'
        },
        {
            'title' : 'P2',
            'artist' : 'Lil Uzi Vert',
            'year' : '2020'
        }
    ]
    context = {'mytop': my_top5}
    return render(request, "blog/index.html", context)
