from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer
from dj_rest_auth.views import LoginView, LogoutView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from dj_rest_auth.registration.views import RegisterView

# Register a new user (inherits from dj-rest-auth's RegisterView)
class RegisterUserView(RegisterView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# List of all users (you can add more fields or filters if needed)
class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


# User detail view (to view a single user's info)
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user  # To fetch the current authenticated user's details


# Custom Login View (using JWT)
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


# Custom Logout View (revoking JWT token)
class CustomLogoutView(LogoutView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            # Blacklist the refresh token (if using blacklisting)
            request.user.auth_token.delete()  # This deletes the JWT token from the user session
            return Response({"detail": "Successfully logged out."}, status=200)
        except Exception as e:
            return Response({"detail": "Logout failed."}, status=400)
