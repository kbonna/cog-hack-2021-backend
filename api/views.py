import matplotlib.pyplot as plt
from django.shortcuts import render
import os
from fer import FER
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Face
from .serializers import FaceSerializer


class FaceView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        faces = Face.objects.all()
        serializer = FaceSerializer(faces, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = FaceSerializer(data=request.data)
        if serializer.is_valid():
            print("Valid photo")
            # Save photo to file
            serializer.save()
            # Get emotions
            image_file = os.curdir + serializer.data["image"]
            image = plt.imread(image_file)
            detector = FER(mtcnn=True)
            response_data = detector.detect_emotions(image)[0]
            # Remove photo
            os.remove(image_file)
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            print("Invalid photo", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
