from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class IndexView(APIView):
	def get(self, request, *args, **kwargs):
		return render(request, "theme/index.html", {})

	def post(self, request, *args, **kwargs):

		return Response({'status': 200})