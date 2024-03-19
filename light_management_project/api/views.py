from rest_framework.views import APIView
from rest_framework.response import Response
from itertools import combinations
from rest_framework import generics

from .serializers import LightCalculateSerializer, RoomLightsSerializer
from .models import Room

# Create your views here.

def find_light_combinations(light_brightness_list, expected_brightness):
    result = []

    def generate_combinations(index, total, combination):
        if total == expected_brightness:
            result.append(combination)
            return
        if total > expected_brightness or index >= len(light_brightness_list):
            return
        generate_combinations(index, total + light_brightness_list[index], combination + [light_brightness_list[index]])
        generate_combinations(index + 1, total, combination)

    generate_combinations(0, 0, [])

    return result



class LightsManage(APIView):
    def post(self, request):
        serializer = LightCalculateSerializer(data=request.data)
        
        if serializer.is_valid():
            light_brightness_list = serializer.validated_data['light_brightness_list']
            expected_brightness = serializer.validated_data['expected_brightness']
            
            combinations_list = find_light_combinations(light_brightness_list, expected_brightness)
            print(find_light_combinations(light_brightness_list, expected_brightness))
            return Response({'result': combinations_list})
        else:
            return Response(serializer.errors, status=400)
        
class RoomLightsAPIView(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomLightsSerializer
    lookup_field = 'pk'