
from django.shortcuts import render
from django.http import HttpResponse
from .models import testURLs
# Create your views here.
 
def index(request):
    all_urls=testURLs.objects.all()
    output=", ".join(q.urlAddress for q in all_urls)
    return HttpResponse("good job!!")

def resAll(request):
    all_urls=testURLs.objects.all()
    context={"object_list":all_urls}
    #output=", ".join(q.urlAddress for q in all_urls)
    #return HttpResponse(output)
    return render(request,"polls/listURL.html",context)

#def allResults(request):
    
 #   return HttpResponse('following are added urls')

def createpostURL(request):
        if request.method == 'POST':
            if request.POST.get('inputURL'):
                post=testURLs()
                post.urlAddress= request.POST.get('inputURL')
                post.save()
            
                return render(request, 'polls/createURL.html')  

        else:
                return render(request,'polls/createURL.html')


