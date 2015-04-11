from django.http import HttpResponse
from django.template import RequestContext,loader
from django.shortcuts import render
from django import forms

class CodeForm(forms.Form):
	data=forms.CharField(label='data',max_length=100)
	code=forms.CharField(label='code',max_length=100)

def mean(data):
	return sum(data)/len(data)

def home(request):
	if request.method=='POST':
		form=CodeForm(request.POST)
		if form.is_valid():
			data0=form.cleaned_data['data']
			data=[float(x) for x in data0.split(',')]
			code=form.cleaned_data['code']
			exec 'result='+code
			return render(request,'template.html',{'data':data0,'code':code,'result':result})
	form=CodeForm()
	return render(request,'template.html',{'form':form,'data':'2015,4,11','code':'sum(data[:2])'})
