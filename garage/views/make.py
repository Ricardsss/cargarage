from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


from ..models import Make


@csrf_exempt
def get_all_makes(request):
    makes = Make.objects.all()

    makes_list = [{"id": make.id, "name": make.name} for make in makes]

    return JsonResponse(makes_list, safe=False, status=200)


class MakeView:

    @csrf_exempt
    def makes(request):
        if request.method == "GET":
            return get_all_makes(request)
        else:
            return JsonResponse({"error": "Only GET method allowed"}, status=405)
