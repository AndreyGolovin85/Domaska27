import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

from avito import settings
from user.models import User, Location


class UserListView(ListView):
    model = User
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        super().get(self, *args, **kwargs)
        self.object_list.order_by("username")
        paginator = Paginator(object_list=self.object_list, per_page=settings.TOTAL_ON_PAGE)
        page = request.GET.get("page")
        page_obj = paginator.get_page(page)
        result = []
        for user in page_obj:
            result.append({"id": user.id,
                           "username": user.username,
                           "first_name": user.first_name,
                           "last_name": user.last_name,
                           "role": user.role,
                           "age": user.age,
                           "ads_count": user.ads.count()})

        return JsonResponse({"user": result, "page": page_obj.number, "total": page_obj.paginator.count},
                            safe=False, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class UserCreateView(CreateView):
    model = User
    fields = ["username", "password", "first_name", "last_name", "role", "locations"]

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)

        user = User.objects.create(
            username=data["username"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            role=data["role"],
            password=data["password"],
            age=data["age"]
        )
        for loc in data["locations"]:
            location, _ = Location.object.get_or_create(name=loc)
            user.location.add(location)

        return JsonResponse({"id": user.id, "username": user.username, "first_name": user.first_name,
                             "last_name": user.last_name, "role": user.role, "password": user.password,
                             "age": user.age, "location": [str(u) for u in user.location.all()]},
                            safe=False, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class UserUpdateView(UpdateView):
    model = User
    fields = ["username", "first_name", "last_name", "role", "password", "age"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        data = json.loads(request.body)
        self.object.username = data["username"]
        self.object.first_name = data["first_name"]
        self.object.last_name = data["last_name"]
        self.object.role = data["role"]
        self.object.password = data["password"]
        self.object.age = data["age"]
        self.object.seve()
        return JsonResponse({"username": self.object.username, "first_name": self.object.first_name,
                             "last_name": self.object.last_name, "role": self.object.role, "password": self.object.password,
                             "age": self.object.age}, safe=False, json_dumps_params={"ensure_ascii": False})


class UserDetailView(DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        return JsonResponse({"id": user.id, "username": user.name, "first_name": user.first_name,
                             "last_name": user.last_name, "role": user.role, "age": user.age},
                            safe=False, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class UserDeleteView(DeleteView):
    model = User
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse({}, status=200)
