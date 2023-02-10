from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from house_app.models import House
from house_app.serializers import HouseSerializer
import requests


def get_houses(number):
    s = requests.Session()
    url = 'http://prod1.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/pp-monthly-update.txt'
    houses = []
    with s.get(url, headers=None, stream=True) as resp:
        for i, line in enumerate(resp.iter_lines()):
            if i == number:
                break
            if line:
                houses.append(line.decode("utf-8").split(','))
    return houses


@api_view(["GET"])
def HouseView(request, format=None):
    try:
        data = get_houses(100)
        house_list = []
        for house in data:
            (
                field_1,
                field_2,
                field_3,
                field_4,
                field_5,
                field_6,
                field_7,
                field_8,
                field_9,
                field_10,
                field_11,
                field_12,
                field_13,
                field_14,
                field_15,
                field_16,
                *rest,
            ) = house

            house_list.append(House(
                field_1=field_1,
                field_2=field_2,
                field_3=field_3,
                field_4=field_4,
                field_5=field_5,
                field_6=field_6,
                field_7=field_7,
                field_8=field_8,
                field_9=field_9,
                field_10=field_10,
                field_11=field_11,
                field_12=field_12,
                field_13=field_13,
                field_14=field_14,
                field_15=field_15,
                field_16=field_16,
            ))
        House.objects.bulk_create(house_list)
    except Exception as e:
        raise ValueError(f"[ERROR]: {e}")
    return Response({"message": "success! database uploaded"}, status=status.HTTP_200_OK)


@api_view(["GET"])
def HouseListView(request, format=None):
    house_list = House.objects.all()
    serializer = HouseSerializer(house_list, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def HouseCreateView(request):
    serializer = HouseSerializer(data=request.data)
    if serializer.is_valid(raise_exception=ValueError):
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PATCH", "DELETE"])
def HouseView(request, pk):
    try:
        house = House.objects.get(pk=pk)
    except House.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = HouseSerializer(house, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "DELETE":
        house.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == "PATCH":
        serializer = HouseSerializer(instance=house, data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
