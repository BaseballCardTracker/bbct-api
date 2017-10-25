from django.core import serializers
from django.http.response import JsonResponse
from django.views import View


class ModelListView(View):
    model_class = None

    def get(self, request):
        objects = self.model_class.objects.all()
        json = serializers.serialize('json', objects)
        return JsonResponse(json, safe=False)
