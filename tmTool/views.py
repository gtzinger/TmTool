from django.shortcuts import render, redirect

from tmTool.models import Activity

from django.views.generic import ListView, CreateView, DeleteView
from django.forms import ModelForm


class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = ['name']
        
def activity_list(request, template_name='activity_list.html'):
    activities = Activity.objects.all()
    data = {}
    data['object_list'] = activities
    return render(request, template_name, data)


def activity_create(request, template_name='activity_form.html'):
    form = ActivityForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('activity_list')
    return render(request, template_name, {'form':form})


class ActivityDelete(DeleteView):
    model = Activity
    fields = ['name']
    