from django.shortcuts import render,redirect
from .models import CommentData

# Create your views here.
def commentview(request):
    if request.method=='GET':
        comm = CommentData.objects.all().order_by('-id')
        # comm = reversed(list(comm)) 
        return render(request,'comment.html',{'comm':comm})
    else:
        CommentData(
        comment = request.POST['comment']
        ).save()

        return redirect(commentview)
