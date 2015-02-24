#-*-coding:utf8-*-
from django import forms
from django.template import loader,RequestContext
from django.http import HttpResponse
from django.shortcuts import render
from ascore import *

class WordForm(forms.Form):
    word=forms.CharField(max_length=10)

def home(request):
#    return HttpResponse('test')
    if request.method=='POST':
        form=WordForm(request.POST)
        if form.is_valid():
            word=form.cleaned_data['word']
            relation='nsubj'
            freq=sort_by_freq(word,relation)[:9]
            dice=sort_by_dice(word,relation)[:9]
            context=RequestContext(request,{'word':word,'relation':relation,'freq':freq,'dice':dice})
            template=loader.get_template('table.html')
            return HttpResponse(template.render(context))

            res=str()
            #for w2 in [u'有趣',u'樂',u'愉',u'愉快',u'美好',u'相處']:
            for w2 in [u'時常',u'勤',u'常',u'常常',u'恆']:
                res+=w2+str(Dist(word,w2))+'<br>'
            return HttpResponse(res)
    form=WordForm()
    return render(request,'table.html',{'form':form})
