import json
from django.core import serializers
from django.http.response import JsonResponse
from django.views import View


class ModelListView(View):
    model_class = None

    def get(self, request):
        models = self.model_class.objects.all()
        if request.GET:
            query_params = {key + '__icontains': request.GET[key] for key in request.GET}
            models = models.filter(**query_params)

        model_json = serializers.serialize('json', models)
        return JsonResponse(model_json, safe=False)

    def post(self, request):
        fields = json.loads(request.body)
        model = self.model_class.objects.create(**fields)
        model_json = serializers.serialize('json', [model])
        return JsonResponse(model_json, safe=False)
