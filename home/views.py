from home.models import table
from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

#----------------Login---------------------
def login(req):
    if req.POST:
        signup = req.POST['signup']
        return redirect('registration')
    if req.POST:
        em = req.POST['em']
        ps = req.POST['pass']
        
        try:
            var = table.objects.get(email = em)
            print(var)
            if var.c_pass == ps:
                req.session['table'] = var.id
                return redirect('dashboard')
            else:
                return HttpResponse('<h1><a href "">You have entered wrong password...</a></h1>')
        except:
             return HttpResponse('<h1><a href "">You are entered wrong email...</a></h1>')
    
    return render(req,'login.html')
#----------------Registration------------------
def registration(req):
    if req.POST:
        nm = req.POST['nm']
        em = req.POST['em']
        nos = req.POST['nos']
        pass1 = req.POST['pass']
        pass2 = req.POST['re_pass']
        try:
            var = table.objects.get(email = em)
            return HttpResponse('<h1><a href "">User already exist...</a></h1>')
        except:
            if pass1 == pass2:
                obj = table()
                obj.name = nm
                obj.email = em
                obj.num = nos
                obj.c_pass = pass2
                obj.save()
            else:
                return HttpResponse('<h1><a href ""> Password are not match </h1>')
    return render(req,'regi.html')

def dashboard(req):
    if 'table' in req.session.keys():
        User = table.objects.get(id = int(req.session['table']))
        if req.POST:
            logout = req.POST['logout']
            return redirect('login')
        return render(req,'dashboard.html',{'USERS':User})
    else:
        return redirect('login')
