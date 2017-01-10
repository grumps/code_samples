from django.shortcuts import get_object_or_404

from rest_framework import permissions, viewsets, status
from rest_framework.response import Response

from events.models import Event, EventType
from events.permissions import IsOwnerOfEvent
from events.serializers import EventSerializer, EventTypeSerializer


class EventTypeViewSet(viewsets.ReadOnlyModelViewSet):

    """
    ReadOnlyModelViewSet for eventtype endpoint.
    """
    model = EventType
    serializer_class = EventTypeSerializer
    queryset = EventType.objects.all()


class EventViewSet(viewsets.ModelViewSet):

    """
    Event Views supports nested operations from within a wedding object.
      * Lists
      * Detail object
      * Update
    """
    # We use class prpoperty querset, so we have a cached query, to work with.
    queryset = Event.objects.prefetch_related('wedding__accounts').all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOfEvent]
    lookup_url_kwarg = 'wedding_pk'

    def get_queryset(self, request):
        queryset = self.queryset.filter(wedding__accounts=request.user)
        return queryset

    def list(self, request, **kwargs):
        if kwargs is not None:
            wedding_pk = kwargs.get('wedding_pk')
        # we add a wedding_pk for handling nested relationships.
        if wedding_pk:
            queryset = self.get_queryset(request).filter(wedding_id=wedding_pk)
        else:
            queryset = self.get_queryset(request)
        serializer_class = EventSerializer
        serialized = serializer_class(queryset, many=True)
        return Response(serialized.data)

    def update(self, request, *arg, **kwargs):
        """
        handles updating event objects
        """
        if kwargs is not None:
            wedding_pk = kwargs.get('wedding_pk')
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(wedding_id=wedding_pk)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, **kwargs):
        """
        append wedding_pk to the event object
        returns: 201 if successful
                 400 if not successful
        """
        if kwargs is not None:
            wedding_pk = kwargs.get('wedding_pk')
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save(wedding_id=wedding_pk)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None, **kwargs):
        """
        handles detail request
        """
        event = get_object_or_404(
            self.queryset, pk=pk, wedding__accounts=request.user)
        serializer_class = EventSerializer
        serialized = serializer_class(event)
        return Response(serialized.data)
