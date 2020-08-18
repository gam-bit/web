from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')


def result(request):
    
    stc = request.POST['content']
    
    letter_cnt_including_spaces = len(stc)
    letter_cnt_excluding_spaces = len(stc.replace(' ', ''))

    return render(request, 'result.html', {'letter_cnt_including_spaces': letter_cnt_including_spaces, 'letter_cnt_excluding_spaces': letter_cnt_excluding_spaces})