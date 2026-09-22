from django.http import HttpResponse
from django.shortcuts import redirect
import time

class UnderMaintenanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/loan_view':
            return HttpResponse('This page is under maintenance. Please try later')
        response = self.get_response(request)
        return response


class denied_admin_panel:
    def __init__(self,get_response):
        self.get_response=get_response

    
    def __call__(self,request):
        if request.path.startswith("/admin/") and not request.user.is_authenticated:
             return HttpResponse("Access Denied")
        response=self.get_response(request)
        return response
    
    
class custom_middlewere:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        print("Request Started")
    
        response=self.get_response(request)
        print("View End")
        return response


class request_time_middleware:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        
        c_time=time.time()
        response=self.get_response(request)
        e_time=time.time()
        print("Total Time required is {}".format(e_time-c_time))
        print("Respone Code :{}".format(response.status_code))

        return response
