from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api_2 import serializers


class HelloApiView(APIView):
    """Teste API view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format = None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get,post,patch,put,delete)',
            'Is similar to a tradicional Django View',
            'Gives you most control over you applicantion logic',
            'Is mapped manually to URLS',
        ]

        return Response({'message':'Hello!','an_apiview': an_apiview })

    def post(self, request):
        """Create a hello mesage with out name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.erros,
            status=status.HTTP_400_BAD_REQUEST
            )

    def put (self, request, pk = None):
        """Handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object """
        return Response ({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Handle delete of an object"""
        return Response ({'method':'DELETE'})
