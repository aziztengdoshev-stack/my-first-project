from django.shortcuts import render, redirect
from ..logic.teacher_crud import TeacherCRUD

crud = TeacherCRUD()

def main_portal(request):
    # Если учитель не вошел — отправляем на логин (проверка сессии)
    teacher_id = request.session.get('teacher_id')
    if not teacher_id:
        return redirect('teacher_login')

    # Данные для отображения
    classes = crud.get_classes()
    selected_class = request.GET.get('class_id') # Учитель выбрал класс в списке
    students = []
    
    if selected_class:
        students = crud.get_students_by_class(selected_class)

    # ОБРАБОТКА ДЕЙСТВИЙ (POST запросы)
    if request.method == "POST":
        action = request.POST.get('action')
        
        if action == "add_grade":
            sid = request.POST.get('student_id')
            sub = request.POST.get('subject')
            gr = request.POST.get('grade')
            crud.set_grade(sid, sub, gr)
            return redirect(f'/teacher/?class_id={selected_class}')

    return render(request, 'teacher_portal.html', {
        'classes': classes,
        'students': students,
        'selected_class': selected_class
    })