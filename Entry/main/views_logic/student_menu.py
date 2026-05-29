from django.shortcuts import render, redirect
from ..logic.student_crud import StudentCRUD

crud = StudentCRUD()

def menu_view(request):
    # Допустим, мы храним ID ученика в сессии после входа
    sid = request.session.get('user_id')
    if not sid:
        return redirect('login') # Если не вошел — на выход

    student = crud.get_profile(sid)
    
    # Обработка действий (если нажали на кнопки в меню)
    action = request.GET.get('action')
    context = {'student': student}

    if action == 'profile':
        return render(request, 'student/profile.html', context)
    elif action == 'grades':
        context['grades'] = crud.get_grades(sid)
        return render(request, 'student/grades.html', context)
    elif action == 'classmates':
        context['classmates'] = crud.get_classmates(student['class_id'], sid)
        return render(request, 'student/classmates.html', context)
    
    return render(request, 'student_menu.html', context)