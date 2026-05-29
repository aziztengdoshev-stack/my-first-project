from django.shortcuts import render, redirect
from ..logic.db_helper import query_db

def login_s(request):
    if request.method == 'POST':
        login_val = request.POST.get('login')
        pass_val = request.POST.get('password')
        
        user = query_db(
            "SELECT * FROM users WHERE login=? AND password=? AND role='student'", 
            [login_val, pass_val], 
            fetchone=True
        )
        
        if user:
            request.session['student_id'] = user['id']
            return redirect('student/menu')
        else:
            return render(request, 'student/login.html', {'error': 'Ошибка доступа или неверные данные'})
            
    return render(request, 'student/login.html')


def login_t(request):
    print("--- Кнопка нажата! ---")
    
    if request.method == 'POST':
        l = request.POST.get('login')
        p = request.POST.get('password')
        print(f"Пытаюсь войти с логином: {l} и паролем: {p}")
        
        if l == 'admin' and p == 'admin123':
            print("Пароль верный! Делаю редирект...")
            request.session['is_admin'] = True
            return redirect('dir/menu')
        else:
            print("Пароль НЕВЕРНЫЙ или роль не найдена.")
            
    return render(request, 'teacher/login.html')