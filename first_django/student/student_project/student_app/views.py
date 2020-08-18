from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')


def result(request):
    
    # dummy data
    students = ['강민지', '강동구', '김강원', '김기범', '김신영',
                '노재민', '최다인', '김바롬', '박한음', '박성찬',
                '박승규', '배성빈', '배진우', '양창원', '정요셉']
    
    name = request.POST['username']
        
    is_exist = False
    if name in students:
        is_exist = True

    return render(request, 'result.html', {'username':name, 'is_exist': is_exist})