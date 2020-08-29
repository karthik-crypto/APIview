from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from APIapp.serializers import  helloserilaizer

class helloAPIView(APIView):

    def get(self,request,format=None):
        an_APIView=[
            'uses as function(get,put,patch)'
        ]

        return Response({'message':'hello','an_APIView':an_APIView})


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
     
