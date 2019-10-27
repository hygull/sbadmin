from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class LoginView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/login.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class RegisterView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/register.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class ForgotPasswordView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/forgot-password.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class LogoutView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/forgot-password.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class ChartsView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/charts.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class TablesView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/tables.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class LogoutView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/forgot-password.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class ButtonsView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/buttons.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class CardsView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/cards.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class PageNotFoundView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/404.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class BlankView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/blank.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class ColorsView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/utilities-color.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class BordersView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/utilities-border.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class AnimationsView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/utilities-animation.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})


class OthersView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "theme/utilities-other.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})



class DashboardView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "users/dashboard.html", {})

    def post(self, request, *args, **kwargs):

        return Response({'status': 200})
