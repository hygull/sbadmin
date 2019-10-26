from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class LoginView(APIView):
	def get(self, request, *args, **kwargs):
		return render(request, "theme/index.html", {})

	def post(self, request, *args, **kwargs):

		return Response({'status': 200})


class SignUpView(APIView):
	def get(self, request, *args, **kwargs):
		return render(request, "users/signup.html", {})

	def post(self, request, *args, **kwargs):

		return Response({'status': 200})


class ForgotPasswordView(APIView):
	def get(self, request, *args, **kwargs):
		return render(request, "users/forgot_password.html", {})

	def post(self, request, *args, **kwargs):

		return Response({'status': 200})


class DashboardView(APIView):
	def get(self, request, *args, **kwargs):
		return render(request, "users/dashboard.html", {})

	def post(self, request, *args, **kwargs):

		return Response({'status': 200})
