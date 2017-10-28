from django.core import serializers
from django.http.response import JsonResponse
from django.views import View


class ModelListView(View):
    model_class = None

    def get(self, request):
        models = self.model_class.objects.all()
        json = serializers.serialize('json', models)
        return JsonResponse(json, safe=False)

    def post(self, request):
        fields = request.POST
        model = self.model_class.objects.create(**fields)
        json = serializers.serialize('json', [model])
        return JsonResponse(json, safe=False)
