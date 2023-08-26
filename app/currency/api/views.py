from rest_framework.generics import ListAPIView
from currency.models import Rate, ContactUs, Source, RequestResponseLog
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RateSerializer


@api_view(['GET'])
def demo_view(request):
    return Response({"message": "Hello, World"})


class RateListAPIView(ListAPIView):
    queryset = Rate.objects.all().order_by('-created')
    serializer_class = RateSerializer