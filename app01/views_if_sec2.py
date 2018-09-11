import time, hashlib


def user_sign(request):
    if request.method == "POST":
        client_time = request.POST.get("time", "")
        client_sign = request.POST.get("sign", "")
    else:
        return "error"
    if client_sign == "" or client_time == "":
        return "sign null"
    now_time = time.time()
    server_time = str(now_time).split(".")[0]
    time_difference = int(server_time) - int(client_time)
    if time_difference >= 60:
        return "timeout"

    md5 = hashlib.md5()
    sign_str = client_time + "&guest"
    sign_byte = sign_str.encode("utf-8")
    md5.update(sign_byte)
    server_sign = md5.hexdigest()
    if server_sign == client_sign:
        return "success"
