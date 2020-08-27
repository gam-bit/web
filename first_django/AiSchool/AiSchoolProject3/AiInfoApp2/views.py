from django.shortcuts import render, redirect
from .models import AiClass, AiStudent, StudentPost
from django.contrib.auth.models import User
from django.contrib import auth

ERROR_MSG = {
    'ID_EXIST': "이미 사용 중인 아이디입니다.",
    'ID_NOT_EXIST': "존재하지 않는 아이디입니다.",
    'ID_PW_MISSING': "아이디와 비밀번호를 확인하세요.",
    'PW_CHECK' : "비밀번호가 일치하지 않습니다."
}

# Create your views here.
def home(request):

    class_object = AiClass.objects.all()
    context = {'class_object': class_object}

    return render(request, 'home.html', context)

def detail(request, class_pk):
    
    class_object = AiClass.objects.get(pk=class_pk)
    context = {
        'class_object': class_object,
        }

    return render(request, 'detail.html', context)

def add(request, std_pk):

    user = AiStudent.objects.get(pk=std_pk)
    
    if request.method == "POST":    
        
        StudentPost.objects.create(
            writer=user,
            intro=request.POST['intro']
        )
        
        return redirect('student', std_pk)


    return render(request, 'add.html', {'std_pk': std_pk})


    
def student(request, std_pk):
    
    student = AiStudent.objects.get(pk=std_pk)
    context = {'student': student}

    return render(request, 'student.html', context)



def edit(request, std_pk):
    
    if request.method == 'POST':
        target_student = AiStudent.objects.filter(pk=std_pk)
        target_student.update(
            name = request.POST['name'],
            sex = request.POST['sex'],
            phone_num = request.POST['phone_num']
        )
        return redirect('student', std_pk)

    student = AiStudent.objects.get(pk=std_pk)
    context = {'student': student}

    return render(request, 'edit.html', context)


def delete(request, std_pk):
    
    student = AiStudent.objects.get(pk=std_pk)
    class_pk = student.class_num
    student.delete()

    return redirect('detail', class_pk) # detail에 있는 변수명과 일치시키기


# authentication

def signup(request): 
    context = {
        'error': {
            'state': False,
            'msg': '',
        }
    }
    
    if request.method == "POST":
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']
        user_pw_check = request.POST['user_pw_check']

        std_name = request.POST['name']
        class_num = request.POST['class_num']
        std_sex = request.POST['sex']
        std_phone_num = request.POST['phone_num']

        user = User.objects.filter(username=user_id)
        

        if len(user) == 0:
    
            if user_id and user_pw:

                if user_pw == user_pw_check:
                    user = User.objects.create_user(
                        username=user_id,
                        password=user_pw
                    )

                    AiStudent.objects.create(
                        user=user,
                        participate_class=AiClass.objects.get(pk=class_num),
                        name=std_name,
                        sex=std_sex,
                        phone_num=std_phone_num
                    )

                    auth.login(request, user)
                    return redirect('home')

                else:
                    context['error']['msg'] = ERROR_MSG['PW_CHECK']
                    context['error']['state'] = True
                
            else:
                context['error']['msg'] = ERROR_MSG['ID_PW_MISSING']
                context['error']['state'] = True
            
        else:
            context['error']['msg'] = ERROR_MSG['ID_EXIST']
            context['error']['state'] = True

    return render(request, 'signup.html', context)



def login(request):
    context = {
        'error': {
            'state': False,
            'msg': '',
        }
    }
    
    if request.method == "POST":

        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']

        user = User.objects.filter(username=user_id)

        if user_id and user_pw:      
            if len(user) > 0:
                
                user = auth.authenticate(
                    username=user_id,
                    password=user_pw
                )
                
                if user != None:
                    auth.login(request, user)
                    return redirect('home')   
                
                else:
                    context['error']['msg'] = ERROR_MSG['PW_CHECK']
                    context['error']['state'] = True          

            else:
                context['error']['msg'] = ERROR_MSG['ID_NOT_EXIST']
                context['error']['state'] = True   
        else: 
            context['error']['msg'] = ERROR_MSG['ID_PW_MISSING']
            context['error']['state'] = True    

    return render(request, 'login.html', context)



def logout(request):
    auth.logout(request)
    return redirect('home')