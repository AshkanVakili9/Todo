
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from drf_spectacular.utils import extend_schema, extend_schema_view


@extend_schema_view(
    list=extend_schema(
        description="The list action returns all available actions."
    ),
    create=extend_schema(
        description="The create action expects the fields `title and description`, creates a new object and returns it."
    ),
    retrieve=extend_schema(
        description="The retrieve action returns a single object selected by `id`."
    )
)
class TodoViewSet(ViewSet):
    """
    Example empty view set demonstrating the standard
    actions that will be handled by a router class.

    If you're using format suffixes, make sure to also include
    the `format=None` keyword argument for each action.
    """
    serializer_class = TodoSerializer

    def list(self, request, format=None):
        data = Todo.objects.all()
        serializer = self.serializer_class(data, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        found_item = Todo.objects.filter(id=pk).first()
        if found_item:
            serializer = self.serializer_class(found_item).data
            return Response(serializer, status=status.HTTP_200_OK)
        return Response("no data with that id found", status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        queryset = Todo.objects.filter(id=pk).first()
        new_data = request.data
        if queryset:
            serializer = TodoSerializer(queryset, new_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("no data with that id found", status=status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, pk=None):
        queryset = Todo.objects.filter(id=pk).first()
        new_data = request.data
        if queryset:
            serializer = TodoSerializer(queryset, new_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("no data with that id found", status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        found_item = Todo.objects.filter(id=pk).first()
        if found_item:
            found_item.delete()
            return Response('item deleted', status=status.HTTP_201_CREATED)
        return Response("no data with that id found", status=status.HTTP_404_NOT_FOUND)
