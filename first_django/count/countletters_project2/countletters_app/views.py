from django.shortcuts import render
import re

# Create your views here.
def home(request):
    return render(request, 'home.html')


def result(request):

    stc = request.POST['content']
    cnt_letters_including_spaces = len(stc.replace('\r', ''))
    cnt_letters_excluding_spaces = len(stc.replace('\n', '').replace('\r', '').replace(' ',''))
    print(cnt_letters_excluding_spaces)
    return render(request, 'result.html', 
                {'cnt_letters_including_spaces': cnt_letters_including_spaces, 
                 'cnt_letters_excluding_spaces': cnt_letters_excluding_spaces})
    