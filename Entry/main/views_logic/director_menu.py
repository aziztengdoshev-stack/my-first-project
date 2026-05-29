from django.shortcuts import redirect
from ..logic.director_crud import DirectorCRUD

crud=DirectorCRUD()

def handle_action(request):
    """Эта функция заменяет все твои if c=='1' и input()"""
    if request.method=="POST":
        role=request.POST.get('role')
        uid=request.POST.get('user_id')
        action=request.POST.get('action')
        
        crud.manage_user(role, uid, action)
    
    return redirect('director_dashboard')