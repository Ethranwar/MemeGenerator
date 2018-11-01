from django.shortcuts import render
from django.urls import reverse
from .models import MemeGenerator
from.forms import SentenceForm
from django.http import HttpResponseRedirect
# Create your views here.
def get_meme(request):
    big_list=[]
    if request.method=="POST":
        form=SentenceForm(request.POST)
        if form.is_valid():
            count=0
            li = [i for i in str(form.cleaned_data['original_sentence'])]
            other_li=[i for i in str(form.cleaned_data['changed_to_sentence'])]
            del other_li[0]    
            while True:
                if li[-1]==' ':
                    del li[-1]
                    continue
                elif len(li)==1:
                    big_list.append(li[0])
                    break
                big_list.append(''.join(li))
                del li[-1]   
            while True:
                if count==len(other_li):
                    break
                elif other_li[count]==' ':
                    li.append(' ')
                    count+=1
                    continue
                li.append(other_li[count])
                big_list.append(''.join(li))
                count+=1
            #big_list now has list of strings to print
    else:
        form=SentenceForm()
    
    context={
        'form':form,
        'big_list':big_list
    }
    return render(request,'memegenerator/home.html',context)

    
