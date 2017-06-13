from django.shortcuts import render
from django.http import HttpResponse
from SU.models import Uploader
import traceback
import datetime
# Create your views here.

def viewlist(request):
    em = "old"
    if request.user.is_authenticated() and request.user.is_active:
        print "Pass1"
    else: 
        print "Fail1"
    try:
        rows = Uploader.objects.filter(STATUS="SUBMITTED")
        fields = [ str(field).split('.')[-1] for field in Uploader._meta.get_fields() if str(field).split('.')[-1] not in ['id', 'CLOSEDON', 'FILE',] ]
        fields.extend(['View', 'Decision',])
        data = {}
        data['cols'] = fields
        data['rows'] = rows
    except Uploader.DoesNotExist:
        msg = traceback.format_exc()
        return HttpResponse(msg)
    return render(request, "view_list.html", data)

def view_doc(request):
    id_pri = request.GET.get("id")
    record = Uploader.objects.get(id=id_pri)
    file_content = record.FILE
    response = HttpResponse(file_content)
    response['Content-Disposition'] = 'attachment; filename=%s'%record.FILENAME.replace(" ", "_")
    return response

def approve_doc(request):
    id_pri = request.GET.get("id")
    record = Uploader.objects.get(id=id_pri)
    record.STATUS = "APPROVED"
    record.CLOSEDON = datetime.datetime.now()
    record.save()
    success = "Approved successfully" if Uploader.objects.get(id=id_pri).STATUS == "APPROVED" else "Approval failed.. Approve again"
    return HttpResponse(success)

def reject_doc(request):
    id_pri = request.GET.get("id")
    record = Uploader.objects.get(id=id_pri)
    record.STATUS = "REJECTED"
    record.CLOSEDON = datetime.datetime.now()
    record.save()
    success = "Rejected successfully" if Uploader.objects.get(id=id_pri).STATUS == "REJECTED" else "Rejection failed.. Reject again"
    return HttpResponse(success)