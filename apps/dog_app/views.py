from django.shortcuts import render, redirect
from .models import Dog

# Create your views here.

def index(request):
	dogs = Dog.objects.all()
	return render(request, 'dog_app/index.html', {'dogs': dogs})

def create(request):
	print (request.POST)
	dog = Dog(name=request.POST['name'], breed=request.POST['breed'])
	dog.save()
	return redirect('/')

def edit(request, id):
	dog = Dog.objects.get(id=id)
	return render(request, 'dog_app/edit.html', {'dog': dog})

def update(request, id):
	dog = Dog.objects.get(id=id)
	dog.name = request.POST['name']
	dog.breed = request.POST['breed']
	dog.save()
	return redirect('/')

def delete(request, id):
	dog = Dog.objects.get(id=id)
	dog.delete()
	return redirect('/')