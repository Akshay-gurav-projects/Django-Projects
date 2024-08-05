from django.shortcuts import render,HttpResponseRedirect
from .forms import SignupForm,LoginForm,AddPostForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from .models import Post
from django.contrib.auth.models import Group
# Create your views here.

#home
def home(request):
	posts = Post.objects.all()
	return render(request,"blog/home.html",{'posts':posts})

#About
def about(request):
	return render(request,"blog/about.html")

#Contact
def contact(request):
	return render(request,"blog/contact.html")

#Dashboard
def dashboard(request):
	if request.user.is_authenticated:
		posts = Post.objects.all()	
		return render(request,"blog/dashboard.html",{'posts':posts})
	else:
		return HttpResponseRedirect('/login/')
#logout
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/')

#sign up
def user_signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save()
			group = Group.objects.get(name='Author')
			user.groups.add(group)
			messages.success(request,"Account created successfully !!")
	else:
		form = SignupForm()
	return render(request,"blog/signup.html",{'form':form})

#login
def user_login(request):
	if not request.user.is_authenticated:
		if request.method == 'POST':
			form = LoginForm(request=request , data = request.POST)
			if form.is_valid():
				uname = form.cleaned_data['username']
				upass = form.cleaned_data['password']
				user = authenticate(username=uname,password=upass)
				if user is not None:
					messages.success(request,"Loged In Successfully !!")
					login(request,user)
					return HttpResponseRedirect('/dashboard/')
		else:
			form = LoginForm()
		return render(request,"blog/login.html",{'form':form})
	else:
		return HttpResponseRedirect('/dashboard/')

#add new post
def add_post(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			form = AddPostForm(request.POST)
			if form.is_valid():
				title = form.cleaned_data['title']
				description = form.cleaned_data['description']
				pst = Post(title = title,description=description)
				pst.save()
				messages.success(request,"Post Added Successfully!!")
				form = AddPostForm()
			return render(request,'blog/add_post.html',{'form':form})
		else:
			form = AddPostForm()
			return render(request,'blog/add_post.html',{'form':form})
	else:
		return HttpResponseRedirect('/login/')
	

#update new post
def update_post(request,id):
	if request.user.is_authenticated:
		if request.method == 'POST':
			pi = Post.objects.get(pk=id)
			form = AddPostForm(request.POST,instance=pi)
			if form.is_valid():
				form.save()
				messages.success(request,"Post Update Successfully!!")
		else:
			pi = Post.objects.get(pk=id)
			form = AddPostForm(instance=pi)
		return render(request,'blog/update_post.html',{'form':form})
	else:
		return HttpResponseRedirect('/login/')
	
#delete post
def delete_post(request,id):
	if request.user.is_authenticated:
		if request.method == 'POST':
			gi = Post.objects.get(pk=id)
			gi.delete()
			messages.success(request,"Post Delete Successfully!!")
			return HttpResponseRedirect('/dashboard/')	
	else:		
		return HttpResponseRedirect('/login/')