from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.http import JsonResponse

from .forms import UserForm
from .models import PlatformUser

import serial


def read_serial(port, buadrate):
    ser = serial.Serial(port, buadrate, timeout=10)
    ser.close()
    ser.open()
    ser.flushInput()
    ser.flushOutput()

    while True:
        idq = ser.readline()
        ids = idq.decode('utf-8').strip()
        if len(ids) == 11:
            return ids
# Create your views here.


def user_list(request):
    context = {'user_list': PlatformUser.objects.all()}
    return render(request, "user_register/user_list.html", context)


def user_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = UserForm()
        else:
            user = PlatformUser.objects.get(pk=id)
            form = UserForm(instance=user)
        return render(request, "user_register/user_form.html", {'form': form})
    else:
        if id == 0:
            form = UserForm(request.POST)
        else:
            employee = PlatformUser.objects.get(pk=id)
            form = UserForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/list')


def user_delete(request, id):
    employee = PlatformUser.objects.get(pk=id)
    employee.delete()
    return redirect('/list')


def id(request):
    if request.method == "GET":
        i = read_serial("COM6", 9600)
        data = {"i": i}
        return JsonResponse(data)
