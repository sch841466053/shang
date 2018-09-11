from django.http import JsonResponse
from app01.models import Event
from app01 import views_if_sec
from django.core.exceptions import ValidationError,ObjectDoesNotExist


def add_event(request):
    eid = request.POST.get("eid", "")
    name = request.POST.get("name", "")
    limit = request.POST .get("limit", "")
    status = request.POST.get("status", "")
    address = request.POST.get("address", "")
    start_time = request.POST.get("start_time", "")
    if eid == "" or name == "" or limit == "" or address == "" or status == "" or start_time == "":
        return JsonResponse({"status":10021, "message": "参数错误"})
    result = Event.objects.filter(id=eid)
    if result:
        return JsonResponse({"status": 10022, "message": "发布会id已经存在"})
    result = Event.objects.filter(name=name)
    if result:
        return JsonResponse({"status":10023, "message": "发布会名字已经存在"})
    try:
        Event.objects.create(id=eid,name=name,limit=limit,address=address,status=int(status),start_time=start_time)
    except ValidationError as e:
        error = "start_time format error. It must be in YYYY--MM--DD HH:MM:SS format."
        return JsonResponse({"status": 10024, "message": error})
    return JsonResponse({"status":200, "message": "添加发布会成功"})

#查询发布会接口


def get_event_list(request):
    auth_result = views_if_sec.user_auth(request)
    if auth_result == "null":
        return JsonResponse({"status": 10011, "message": "auth null"})
    if auth_result == "fail":
        return JsonResponse({"status": 10012, "message": "auth fail"})

    eid = request.GET.get("eid", "")
    name = request.GET.get("name", "")
    if eid == "" and name == "":
        return JsonResponse({"status": 10021, "message": "参数错误"})
    if eid != "":
        event = {}
        try:
            result = Event.objects.get(id=eid)
        except ObjectDoesNotExist as e:
            return JsonResponse({"status": 10022, "message": "查询为空"})
        else:
            event["name"] = result.name
            event["limit"] = result.limit
            event["status"] = result.status
            event["address"] = result.address
            event["start_time"] = result.start_time
            return JsonResponse({"status": 200, "message": "成功", "data": event})
    if name != "":
        datas = []
        results = Event.objects.filter(name__contains=name)
        if results:
            for r in results:
                event = {}
                event["name"] = r.name
                event["limit"] = r.limit
                event["status"] = r.status
                event["address"] = r.address
                event["start_time"] = r.start_timer
                datas.append(event)
                return JsonResponse({"status": 200, "message": "成功", "data":datas})
        else:
            return JsonResponse({"status": 10022, "message": "查询为空"})