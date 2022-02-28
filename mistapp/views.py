from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Sorev
from .serializers import SorevSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def sorev_list(request):
    if request.method == 'GET':
        sorevs = Sorev.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            sorevs = sorevs.filter(title__icontains=title)

        sorevs_serializer = SorevSerializer(sorevs, many=True)
        return JsonResponse(sorevs_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        sorev_data = JSONParser().parse(request)
        sorev_serializer = SorevSerializer(data=sorev_data)
        if sorev_serializer.is_valid():
            sorev_serializer.save()
            return JsonResponse(sorev_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(sorev_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Sorev.objects.all().delete()
        return JsonResponse({'message': '{} Sorevs were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def sorev_detail(request, pk):
    try:
        sorev = Sorev.objects.get(pk=pk)
    except Sorev.DoesNotExist:
        return JsonResponse({'message': 'The Sorev does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        sorev_serializer = SorevSerializer(sorev)
        return JsonResponse(sorev_serializer.data)

    elif request.method == 'PUT':
        sorev_data = JSONParser().parse(request)
        sorev_serializer = SorevSerializer(sorev, data=sorev_data)
        if sorev_serializer.is_valid():
            sorev_serializer.save()
            return JsonResponse(sorev_serializer.data)
        return JsonResponse(sorev_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        sorev.delete()
        return JsonResponse({'message': 'Sorevs was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def sorev_list_published(request):
    sorevs = Sorev.objects.filter(published=True)

    if request.method == 'GET':
        sorevs_serializer = SorevSerializer(sorevs, many=True)
        return JsonResponse(sorevs_serializer.data, safe=False)
