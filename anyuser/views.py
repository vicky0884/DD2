from django.shortcuts import render
from django.http import HttpResponse
from SU.models import Uploader
from datetime import datetime

def upload_page(request):
    return render(request, 'upload.html', {'user':'Guest', 'title': 'Upload Page',})# 'csrf_token':csrf_token})

def upload(request):
    email = request.POST.get('email', None)
    mobile = request.POST.get('mobile', None)
    fname = request.FILES['file']
    contents = fname.read()
    fname = str(fname)
    ids = datetime.now().strftime("%Y%m%d%H%M%S%f")
    obj_uploader = Uploader(IDS=ids, EMAIL=email, PHONE=mobile, FILENAME=fname, FILE=contents)
    obj_uploader.save()
    updr = Uploader.objects.filter(IDS=ids)
    success = "Uploaded Successfully" if len(updr) > 0 else "Upload Failed"
    return HttpResponse(success)
