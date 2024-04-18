import requests
from djoser.views import UserViewSet as DjoserUserViewSet
from rest_framework import status, viewsets, response

from rest_framework.permissions import AllowAny

from user.models import User
from palette.models import Palette, Color
from api.serializers import UserSerializer, PaletteSerializer, ColorSerializer


class UserViewset(DjoserUserViewSet):

    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer


class PaletteViewset(viewsets.ModelViewSet):

    queryset = Palette.objects.all()
    serializer_class = PaletteSerializer
    permission_classes = (AllowAny, )


class ColorViewset(viewsets.ModelViewSet):

    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = (AllowAny, )

    def create_color_name(self, hex_code):
        hex = [i for i in hex_code if i[0] != "#"]
        url = f"https://www.thecolorapi.com/id?hex={hex}"
        response_generator = requests.get(url)
        data_name = response_generator.json()
        print(data_name)
        return data_name["name"]["value"]

    def create(self, request):
        data = request.data.copy()
        hex_code = data["hex"]
        data["name"] = self.create_color_name(hex_code)

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return response.Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )
