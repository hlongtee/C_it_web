import json, logging

from django.http import JsonResponse

from .res_code import Code, error_map

# logger = logging.getLogger("django")


# 用于处理json格式转化功能
def to_json_data(errno: object = Code.OK, errmsg: object = '', data: object = None, kwargs: object = None) -> object:
    json_dict = {'errno': errno, 'errmsg': errmsg, 'data': data}

    if kwargs and isinstance(kwargs, dict):
        json_dict.update(kwargs)

    return JsonResponse(json_dict)


# 用与将json格式数据转为dict
def json_to_dict(request):
    try:
        json_data = request.body
        if not json_data:
            return to_json_data(errno=Code.PARAMERR, errmsg=error_map[Code.PARAMERR], data=None)
        dict_data = json.loads(json_data)
        return dict_data
    except Exception as e:
        # logger.info("json转dict失败：\n{}".format(e))
        return to_json_data(errno=Code.UNKOWNERR, errmsg=error_map[Code.UNKOWNERR])
