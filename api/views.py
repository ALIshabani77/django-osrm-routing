from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RouteRequestSerializer
from .services import OSRMService

class ShortestPathView(APIView):
    def post(self, request):
        serializer = RouteRequestSerializer(data=request.data)
        if serializer.is_valid():
            try:
                start = tuple(serializer.validated_data['start'])
                end = tuple(serializer.validated_data['end'])
                
                result = OSRMService.calculate_route(start, end)
                return Response(result, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)