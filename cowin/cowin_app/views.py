from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import json
import copy
from rest_framework.views import APIView
import pdfkit
# Create your views here.


class ByDistrict(APIView):
    def get(self, request, id=None, date=None):
        url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id={id}&date={date}"
        base_request_header = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
            }
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJhZTRjZDAwYS02ZGI4LTQ2NzUtYjgxOS01ZmIxYzBmNWJjYTYiLCJ1c2VyX3R5cGUiOiJCRU5FRklDSUFSWSIsInVzZXJfaWQiOiJhZTRjZDAwYS02ZGI4LTQ2NzUtYjgxOS01ZmIxYzBmNWJjYTYiLCJtb2JpbGVfbnVtYmVyIjo5MzcwNjY3OTg4LCJiZW5lZmljaWFyeV9yZWZlcmVuY2VfaWQiOjgwMjk3OTk2MzY5NzAwLCJ0eG5JZCI6Ijk2NDk2ODFlLTEwYTItNDZkYy04YjIwLTY1ODlhYThkODgyOCIsImlhdCI6MTYyMDQ4NzA1MiwiZXhwIjoxNjIwNDg3OTUyfQ.map0oTewHmBfyEuZItIyTVUYSQ5ac9XBxF3cq10Ipcs"
        headers = copy.deepcopy(base_request_header)
        # headers["Accept"] = "application/json"
        # headers["Authorization"] = "Bearer {token}"
        r = json.loads(requests.get(url, headers=headers).content)
        return Response(r)

class GetCert(APIView):
    def get(self, request):
        url = f"https://cdn-api.co-vin.in/api/v2/registration/certificate/download?beneficiary_reference_id=7486151035182"
        base_request_header = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
            }
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJjMDgwMGQ2OS0xY2M1LTQzZDMtYjZhYy00Y2FlM2MwOWRmY2EiLCJ1c2VyX2lkIjoiYzA4MDBkNjktMWNjNS00M2QzLWI2YWMtNGNhZTNjMDlkZmNhIiwidXNlcl90eXBlIjoiQkVORUZJQ0lBUlkiLCJtb2JpbGVfbnVtYmVyIjo5MzA5OTY0MjQ2LCJiZW5lZmljaWFyeV9yZWZlcmVuY2VfaWQiOjc0ODYxNTEwMzUxODIsInNlY3JldF9rZXkiOiJiNWNhYjE2Ny03OTc3LTRkZjEtODAyNy1hNjNhYTE0NGYwNGUiLCJ1YSI6IlBvc3RtYW5SdW50aW1lLzcuMjguMCIsImRhdGVfbW9kaWZpZWQiOiIyMDIxLTA1LTA4VDIwOjAwOjQxLjkwNFoiLCJpYXQiOjE2MjA1MDQwNDEsImV4cCI6MTYyMDUwNDk0MX0.g3x5EHbENR9ascOJTVJtMFBWOg4TxWZbVwF1PUXtgfQ"
        headers = copy.deepcopy(base_request_header)
        headers["Accept"] = "application/json"
        headers["Authorization"] = "Bearer {token}"
        r = requests.get(url, headers=headers).content
        with open("test.pdf", "wb") as f:
            f.write(r)
        return Response(r)

def index(request):
    return HttpResponse("Hi")
