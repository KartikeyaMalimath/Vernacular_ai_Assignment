from django.shortcuts import render
from km_api_app.serializer.vernacular_schema import finiteSchema, numericSchema
from km_api_app.validator.vernacular_validator import VernacularValidator, Constants
from marshmallow import INCLUDE, ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# #test
from django.http import HttpResponse

# Create your views here.

#test
def hello(request):
    return HttpResponse("Hello world")

class FiniteValues(APIView):
    def post(self, request):
        schema = finiteSchema()
        try:
            fvObj = schema.load(request.data, unknown=INCLUDE)
        except ValidationError as e:
            return Response(data = e.messages, status=status.HTTP_400_BAD_REQUEST)
        else:
            fv = VernacularValidator()
            result = fv.validate_finite_values_entity(**vars(fvObj))
            return Response({Constants.cFilled: result[0], Constants.cPartial : result[1], Constants.cTrigger: result[2], Constants.cParams: result[3]})
    
class NumericConstraints(APIView):
    def post(self, request):
        schema = numericSchema()
        try:
            ncObj = schema.load(request.data, unknown = INCLUDE)
        except ValidationError as e:
            return Response(data = e.messages, status = status.HTTP_400_BAD_REQUEST)
        else:
            nc = VernacularValidator()
            r = nc.validate_numeric_entity(**vars(ncObj))
            return Response({Constants.cFilled : r[0], Constants.cPartial : r[1], Constants.cTrigger : r[2], Constants.cParams : r[3]})