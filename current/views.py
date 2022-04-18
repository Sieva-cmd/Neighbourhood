
import datetime as dt
from django.contrib.auth.decorators import login_required
from django.http  import Http404,HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import  render, redirect,get_object_or_404
from .forms import HoodForm, NewUserForm,UpdateUserForm,UpdateUserProfileForm,UserCreationForm,BusinessForm,PostForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.urls import reverse
from .models import NeighbourHood,Business,Post,Profile

# Create your views here.
def home(request):
    return render(request,'main/home.html')


def neighborhood(request):
	current_user =request.user
	hoods =NeighbourHood.objects.all()
	return render(request, "main/hoods.html",{'hoods':hoods,'current_user':current_user})

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
		
			messages.success(request, "Registration successful." )
			return redirect(login_request)
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="main/register.html", context={"register_form":form})


def new_neighborhood(request):
	if request.method =='POST':
		form =HoodForm(request.POST, request.FILEs)
		if form.is_valid():
			hood =form.save(commit=False)
			hood.save()
			return HttpResponseRedirect(reverse("hoods"))

	else:
		form =HoodForm()
	return render(request, 'main/newhood.html',{'form':form})			
@login_required(login_url='login')
def profile(request, username):
    current_user=request.user
           
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateUserProfileForm(instance=request.user.profile)

    return render(request, 'main/profile.html', {'user_form':user_form,'profile_form':profile_form})

@login_required(login_url='login')
def user_hood(request,id):
    current_user = request.user
    hood = NeighbourHood.objects.get(id=id)
    members = Profile.objects.filter(neighbourhood=hood)
    businesses = Business.objects.filter(neighbourhood=hood)
    posts = Post.objects.filter(neighbourhood=hood)
    request.user.profile.neighbourhood = hood
    request.user.profile.save()
    
    return render(request, 'main/userhood.html', {'hood': hood,'businesses':businesses,
                                                            'posts':posts,'current_user':current_user,
                                                            'members':members})

@login_required(login_url='login')
def leave_hood(request,id):
    hood = NeighbourHood.objects.get(id=id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    return redirect('hoods')															

@login_required(login_url='login')
def update_hood(request,id):
    title = 'UPDATE HOOD'
    instance= NeighbourHood.objects.get(id=id)
    if request.method=='POST':
        form = HoodForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
           form.save()
        messages.success(request, ('Hood Updated Successfullly'))
        return redirect('hoods')
    else:
        form = HoodForm(instance=instance)
    return render(request,'main/newhood.html',{'form':form,'title':title})

@login_required(login_url='login')
def new_business(request,id):
    hood = NeighbourHood.objects.get(id=id)
    title = 'ADD BUSINESS'
    if request.method=='POST':
        bus_form = BusinessForm(request.POST,request.FILES)
        if bus_form.is_valid():
            business = bus_form.save(commit=False)
            business.neighbourhood = hood
            business.owner = request.user.profile
            business.save()
            return redirect('my_hood', id)
    else:
        bus_form = BusinessForm()
    return render(request,'main/business.html',{'bus_form':bus_form,'title':title})

@login_required(login_url='login')
def update_business(request,id,bus_id):
    instance= Business.objects.get(id=bus_id)
    title = 'UPDATE BUSINESS'
    if request.method=='POST':
        bus_form = BusinessForm(request.POST,request.FILES,instance=instance)
        if bus_form.is_valid():
            bus_form.save()
        return redirect('my_hood', id)
    else:
        
        bus_form = BusinessForm(instance=instance)
    return render(request,'main/business.html',{'bus_form':bus_form,'title':title})


@login_required(login_url='login')
def delete_business(request,id,bus_id):
    business= Business.objects.get(id=bus_id)
    business.delete_business()
    messages.info(request, ('Business Deleted'))
    return redirect('my_hood', id)



@login_required(login_url='login')
def new_post(request,id):
    hood = NeighbourHood.objects.get(id=id)
    title = 'ADD POST'
    if request.method=='POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.neighbourhood = hood
            post.owner = request.user
            post.save()
            return redirect('my_hood', id)
    else:
        post_form = PostForm()
    return render(request,'main/post.html',{'post_form':post_form,'title':title})

@login_required(login_url='login')
def update_post(request,id,post_id):
    title = 'UPDATE POST'
    instance= Post.objects.get(id=post_id)
    if request.method=='POST':
        post_form = PostForm(request.POST,instance=instance)
        if post_form.is_valid():
           post_form.save()
        return redirect('my_hood', id)
    else:
        post_form = PostForm(instance=instance)
    return render(request,'main/post.html',{'post_form':post_form,'title':title})


@login_required(login_url='login')
def delete_post(request,id,post_id):
    post= Post.objects.get(id=post_id)
    post.delete_post()
    messages.info(request, ('Post Deleted'))
    return redirect('my_hood', id)




    

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username,password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect(home)
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request,template_name="main/login.html", context={"login_form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect(login_request)      
