from django.shortcuts import render,redirect
from categories import forms
# Create your views here.

def addCategory(request):
    if request.method == 'POST':
        form = forms.addCategory(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addCategory')
    else:
        form = forms.addCategory()
    return render(request, 'addCategory.html', {'form': form})
