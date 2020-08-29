from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from APIapp import serializers

class helloAPIView(APIView):

    def get(self,request,format=None):
        an_APIView=[
            'uses as function(get,put,patch)'
        ]

        return Response({'message':'hello','an_APIView':an_APIView})


        class helloAPIView(APIView):
            serializer_class=serializers.helloserializers



            def post(self,request,format=none):
                serializer=self.serializer_class(data=request.data)

                if serializer. is_valid():
                    name=serializer.validated_data.post('name')
                    message=f'hellp{name}'
                    return Response({'message':'message'})
                else:
                    return Response(
                    status=status.HTTP-400-BAD-REQUEST
                    )



