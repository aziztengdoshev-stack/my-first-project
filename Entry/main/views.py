from django.shortcuts import render
from main.logic import director_crud
from .logic.director_crud import DirectorCRUD
from django.contrib.auth import logout
from django.shortcuts import redirect
from .auth import login_logic
from .views_logic.director_menu import *
from .views_logic.teacher_menu import *
from .views_logic.student_menu import *

db=DirectorCRUD() 

def dir_menu(request):
    return render(request, 'dir/menu.html')

def teach_menu(request):
    return render(request, 'teacher/menu.html')

def login_t(request):
    return render(request, 'teacher/login.html')

def stud_menu(request):
    return render(request, 'student/menu.html')

def login_s(request):
    return render(request, 'student/login.html')

def classes_list(request):
    classes=db.get_all_classes()
    return render(request, 'classes_list.html', {'classes': classes})

def teachers_list(request):
    teachers=db.get_all_teachers()
    return render(request, 'dir/teachers_list.html', {'teachers': teachers})

def manage_class(request, class_id):
    current_class=db.get_class_info(class_id)
    students=db.get_students_by_class(class_id)
    return render(request, 'dir/manage_class.html', {
        'class': current_class,
        'students': students
    })

def manage_teacher(request, teacher_id):
    teacher = db.get_teacher_info(teacher_id)
    
    if teacher is None:
        from django.http import Http404
        raise Http404("Учитель не найден")
        
    return render(request, 'dir/manage_teacher.html', {'teacher': teacher})

def enter_rol(request):
    return render(request, 'enter_rol.html')

def logout_user(request):
    logout(request)
    return redirect('enter_rol')

def login_t(request):
    return login_logic.login_t(request)

def add_teacher_view(request):
    if request.method == "POST":
        f_name = request.POST.get('first_name')
        l_name = request.POST.get('last_name')
        uname = request.POST.get('username')
        pwd = request.POST.get('password')

        crud = DirectorCRUD()
        crud.add_teacher(f_name, l_name, uname, pwd)
        return redirect('teachers_list')
    return render(request, 'dir/add_teacher.html')

def edit_teacher(request, teacher_id):
    if request.method == 'POST':
        f_name = request.POST.get('first_name')
        l_name = request.POST.get('last_name')
        u_name = request.POST.get('username')
        
        db.update_teacher(teacher_id, f_name, l_name, u_name)
        
        return redirect('manage_teacher', teacher_id=teacher_id)
    
    teacher = db.get_teacher_info(teacher_id)
    return render(request, 'dir/edit_teacher.html', {'teacher': teacher})

def delete_teacher(request, teacher_id):
    db.delete_teacher(teacher_id)
    
    return redirect('teachers_list')

def classes_list(request):
    classes = director_crud.query_db("SELECT * FROM school_classes")
    
    return render(request, 'dir/classes_list.html', {'classes': classes})

def add_class(request):
    if request.method == 'POST':
        class_name = request.POST.get('class_name')
        
        if class_name:
            director_crud.query_db("INSERT INTO school_classes (class_name) VALUES (?)", (class_name,))
            
            return redirect('classes_list') 

    return render(request, 'dir/add_class.html')

def add_student(request, class_id):
    if request.method == 'POST':
        fn = request.POST.get('first_name')
        ln = request.POST.get('last_name')
        bd = request.POST.get('birth_date')
        un = request.POST.get('username')
        pw = request.POST.get('password')

        sql = """
            INSERT INTO students (first_name, last_name, class_id, birth_date, username, password) 
            VALUES (?, ?, ?, ?, ?, ?)
        """
        
        director_crud.query_db(sql, (fn, ln, class_id, bd, un, pw))
        
        return redirect('manage_class', class_id=class_id)
    
    return render(request, 'add_student.html', {'class_id': class_id})

def delete_class(request, class_id):
    sql = "DELETE FROM school_classes WHERE id = ?"
    director_crud.query_db(sql, (class_id,))
    return redirect('classes_list')

def edit_class(request, class_id):
    if request.method == 'GET':
        sql = "SELECT * FROM school_classes WHERE id = ?"
        current_class = director_crud.query_db(sql, (class_id,), fetchone=True)
        return render(request, 'dir/edit_class.html', {'class': current_class})

    if request.method == 'POST':
        new_name = request.POST.get('class_name')
        sql = "UPDATE school_classes SET class_name = ? WHERE id = ?"
        director_crud.query_db(sql, (new_name, class_id))
        return redirect('manage_class', class_id=class_id)