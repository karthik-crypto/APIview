from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
<<<<<<< HEAD
from APIapp.serializers import  helloserilaizer
=======

from APIapp.serializers import  helloserilaizer


>>>>>>> 7c9de4e82d545c51d6bece2aacb82e437103b011

class helloAPIView(APIView):

    def get(self,request,format=None):
        an_APIView=[
            'uses as function(get,put,patch)'
        ]

        return Response({'message':'hello','an_APIView':an_APIView})


<<<<<<< HEAD
=======

>>>>>>> 7c9de4e82d545c51d6bece2aacb82e437103b011
class postAPIView(APIView):
    serializer_class=  helloserilaizer
    def post(self,request,format=None):
        serializer=self.serializer_class(data=request.data)
        if serializer. is_valid():
            name=serializer.validated_data.get('name')
            message=f'hello {name}'
            return Response({'message':message})
        else:
            return Response(
                status=status.HTTP-400-BAD-REQUEST
            )
<<<<<<< HEAD


=======
>>>>>>> 7c9de4e82d545c51d6bece2aacb82e437103b011

     
