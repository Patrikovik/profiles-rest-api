from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Teste API view"""
    def get(self, request, format = None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get,post,patch,put,delete)',
            'Is similar to a tradicional Django View',
            'Gives you most control over you applicantion logic',
            'Is mapped manually to URLS',
        ]

        return Response({'message':'Hello!','an_apiview': an_apiview})
