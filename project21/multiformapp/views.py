from django.http import HttpResponse
from django.shortcuts import redirect, render

from multiformapp.forms import FirstStudentInfoForm, SecondStudentInfoForm
from multiformapp.models import StudentInfo

# Create your views here.

def firstpage_view(request):
    if request.method == 'POST':
        form = FirstStudentInfoForm(request.POST)
        if form.is_valid():
            request.session['first_five_fields'] = form.cleaned_data
            return redirect('secondpage')
    else:
        form = FirstStudentInfoForm()

    return render(request, 'multiformapp/firstpage_form.html', {'form': form})

    

def secondpage_view(request):
    if request.method == 'POST':
        form = SecondStudentInfoForm(request.POST)
        if form.is_valid():
            first_five_fields = request.session.get('first_five_fields', {})
            form_data = {**first_five_fields, **form.cleaned_data}
            student_info = StudentInfo(**form_data)
            student_info.save()
            return redirect('thankyou')
    else:
        form = SecondStudentInfoForm()

    return render(request, 'multiformapp/secondpage_form.html', {'form': form})



def thankyou(request):
        return render(request,'multiformapp/thank_you.html')
