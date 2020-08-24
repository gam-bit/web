from django.shortcuts import render, redirect
from .models import AiClass, AiStudent


# Create your views here.
def home(request):

    class_object = AiClass.objects.all()
    context = {'class_object': class_object}

    return render(request, 'home.html', context)

def detail(request, class_pk):
    
    class_object = AiClass.objects.get(pk=class_pk)
    student_object = AiStudent.objects.filter(class_num=class_pk)
    context = {
        'class_pk': class_pk,
        'class_object': class_object,
        'student_object': student_object
        }

    return render(request, 'detail.html', context)

def add(request, class_pk):
    
    class_obj = AiClass.objects.get(pk=class_pk)

    if request.method == "POST":    
        AiStudent.objects.create(
            class_num=class_pk,
            name=request.POST['name'],
            sex=request.POST['sex'],
            phone_num=request.POST['phone_num'],
        )
        
        return redirect('detail', class_pk)


    context = {'class_obj': class_obj}

    return render(request, 'add.html', context)


    
def student(request, std_pk):
    
    student = AiStudent.objects.get(pk=std_pk)
    context = {'student': student}

    return render(request, 'student.html', context)



def edit(request, std_pk):
    
    if request.method == 'POST':
        AiStudent.objects.filter(pk=std_pk).update(
            name = request.POST['name'],
            sex = request.POST['sex'],
            phone_num = request.POST['phone_num'],
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