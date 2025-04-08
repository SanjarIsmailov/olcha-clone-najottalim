from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer
from dj_rest_auth.views import LoginView, LogoutView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from dj_rest_auth.registration.views import RegisterView

class RegisterUserView(RegisterView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class CustomLoginView(LoginView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        # Standard login view (uses dj-rest-auth to authenticate)
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            # Generate JWT tokens and include them in the response
            refresh = RefreshToken.for_user(request.user)
            access_token = str(refresh.access_token)
            data = response.data
            data["access_token"] = access_token
            return Response(data)
        return response

class CustomLogoutView(LogoutView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            request.user.auth_token.delete()
            return Response({"detail": "Successfully logged out."}, status=200)
        except Exception as e:
            return Response({"detail": "Logout failed."}, status=400)
