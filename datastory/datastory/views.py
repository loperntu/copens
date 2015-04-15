#-*-coding:utf8-*-
from django.http import HttpResponse
from django.template import RequestContext,loader
from django.shortcuts import render
from django import forms

class CodeForm(forms.Form):
	data=forms.CharField(label='data',max_length=333)
	code=forms.CharField(label='code',max_length=333)

def mean(data):
	return sum(data)/len(data)

def home(request):
	if request.method=='POST':
		form=CodeForm(request.POST)
		if form.is_valid():
			data0=form.cleaned_data['data']
			data=data0.split('\n')
			code=form.cleaned_data['code']
			exec code
			return render(request,'template.html',{'data':data0,'code':code,'result':output})
	form=CodeForm()
	return render(request,'template.html',{
'form':form,
'data':'''
新加坡,1
首爾,9''',
'code':'''
output=""
d=dict()
for line in data:
    country,rank=line.split(",")
    d[country]=int(rank)
sort=sorted(d.items(),key=lambda (k,v):(v,k))
for country,rank in sort:
    output+=country+u"排名第"+str(rank)+u"。"
'''})
