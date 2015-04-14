#-*-coding:utf8-*-
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
			data=form.cleaned_data['data']
			code=form.cleaned_data['code']
			d=dict()
			for line in data.split('\n'):
				city,rank=line.split(',')
				d[city]=int(rank)
			sort=sorted(d.items(),key=lambda (k,v):(v,k))
			exec code
			return render(request,'template.html',{'data':data,'code':code,'result':output})
	form=CodeForm()
	return render(request,'template.html',{
'form':form,
'data':'Singapore,1\nSeoul,9',
'code':'''
output=""
for country,rank in sort:
    output+=country+" ranks "+str(rank)+". "
'''})
