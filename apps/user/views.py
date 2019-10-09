from django.shortcuts import render, HttpResponse, redirect, reverse
# from django.http import JsonResponse
from django.views import View
from django.db.models import Q, F

from .models import *
from utils.json_data.json_fun import to_json_data, json_to_dict


# Create your views here.
class Get_user(View):

    def get(self, request):
        return HttpResponse('ok')

    def post(self, request):
        dict_data = json_to_dict(request)
        choice = dict_data.get('choice')
        if choice == 0:  # 获取父部
            rs = ParentDepartment.objects.values_list('id', 'parent_name').all()
        elif choice == 1:  # 获取部们
            p_id = dict_data.get('id')
            rs = Department.objects.filter(users__parent_name_id=p_id).values_list('id', 'dep_name')
            rs = list(set(rs))
        elif choice == 2:  # 获取人
            dep_id = dict_data.get('id')
            rs = Users.objects.filter(dep_name_id=dep_id).values_list('id', 'username')
        else:
            rs = []
        data = {}
        for i in range(len(rs)):
            data[rs[i][0]] = rs[i][1]
        return to_json_data(data=data)
