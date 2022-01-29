from django.shortcuts import render,redirect
from .models import Tasks
from django.contrib import messages
from django.contrib.auth.models import User , auth
def Index(request):
    name=request.user
    print(name.username)
    task=Tasks.objects.filter(users=name.id)
    num=Tasks.objects.filter(users=name.id).count # To get number of objects
    #num=Tasks.objects.all().aggregate()
    return render(request,'base.html',{
    'lists':task,'nam':num,'name':name,
    })
def Data(request,ids):
    if(request.method=='GET'):
        dat=Tasks.objects.get(id=ids)
        users=request.user.id
        #dat=users.Task.all()
        return render(request,'data.html',{
            'dat':dat
        })
    else:
        return redirect ('/')
def Button(request):
    if request.method=='POST':
        tn=request.POST['data1']
        tm=request.POST['data2']
        user=request.user
        d=Tasks()
        #usrs=d.users
        d.Title=tn
        d.Desc=tm
        
        d.save()
        d.users.add(user.id)
        return redirect('/')
    else:
        return render(request,'Entry.html')

def Delt(request,idd):
    t=Tasks.objects.get(id=idd)
    t.delete()
    return redirect('/')

def signup(request):
    if request.method == 'POST':
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,)
                user.save();
                print('user created')
                return redirect('login')
        else:
            print('password not matching')
            #return redirect('account/signup.html')
            return redirect('/')
        
    else:
        return render(request,'account/signup.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')
            #return redirect('/')

    else:
        return render(request,'account/login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')