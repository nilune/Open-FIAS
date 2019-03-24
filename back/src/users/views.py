from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from social_django.views import auth as auth_login
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from django.contrib.sessions.backends.db import SessionStore
from django.shortcuts import get_object_or_404
from maps.models import Object
from django.views.decorators.http import require_http_methods
import json


@csrf_exempt
def login(request):
    return auth_login(request, 'openstreetmap')


@csrf_exempt
def logout(request):
    auth_logout(request)
    return JsonResponse({'status': 200})


@csrf_exempt
@login_required
def get_user_detail(request):  # TODO get info about points from OSM
    user = request.user
    data = {'username': user.username}
    extra_data = user.social_auth.get(provider='openstreetmap').extra_data
    data['uid'] = extra_data['id']
    data['avatar'] = extra_data['avatar']
    if 'email' in extra_data:
        data['email'] = extra_data['email']
    user_obj = Object.objects.all().filter(author=user).order_by("-created")
    data['points'] = serialize('json', user_obj)
    return JsonResponse(data)


@csrf_exempt
def check_auth(request):
    response = JsonResponse({'authorization': False, 'points': False})
    if request.user.is_authenticated:
        session = request.session
        if session.session_key is None:
            return HttpResponseBadRequest('Wrong request data - should be session')
        return JsonResponse({'authorization': True, 'points': session['points']})
    if request.session.session_key is None:
        session = SessionStore()
        session['points'] = []
        session.save()
        response.set_cookie('sessionid', session.session_key, httponly=True)
    return response


@csrf_exempt
@login_required
@require_http_methods("POST")
def add_points_from_cookie(request):
    if request.session.session_key is not None:
        session = request.session
        if 'points' not in session:
            return HttpResponseBadRequest('Wrong request data - there are no points')
        if len(session['points']) == 0:
            return HttpResponseBadRequest('Wrong request data - there are no points')
        try:
            data = json.loads(request.body)
        except json.decoder.JSONDecodeError:
            return HttpResponseBadRequest('Wrong request count of fields - bad fields')
        points = data.get('points')
        if points is None:
            return HttpResponseBadRequest('Wrong request count of fields - bad fields')

        for item in points:
            if item not in session['points']:
                return HttpResponseBadRequest('Wrong request data - not correct id')
            obj = get_object_or_404(Object, id=item[0])
            obj.author = request.user
            obj.save()
        del session['points']
        return HttpResponse(True)
    return HttpResponseBadRequest('Wrong request data - should be session')


def clear_sessions():
    SessionStore.clear_expired()


@csrf_exempt
def get_list_last_points(request):
    objects = Object.objects.all().filt_del(request.user).order_by("-created")[:10]
    data = {'points': serialize('json', objects)}
    return JsonResponse(data)


@csrf_exempt
def get_list_points(request):
    data = Object.objects.all().filt_del(request.user)
    return JsonResponse(serialize('json', data))
