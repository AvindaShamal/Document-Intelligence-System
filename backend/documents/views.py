from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView

from .models import Document
from .serializers import DocumentSerializer
from .permissions import IsOwner
from .tasks import process_document


class DocumentUploadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request) -> Response:
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            document = serializer.save(owner=request.user)
            process_document.delay(document.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DocumentListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request) -> Response:
        documents = Document.objects.filter(owner=request.user)
        serializer = DocumentSerializer(documents, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DocumentDetailView(RetrieveAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class DocumentStatusView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]

    def get(self, request, pk) -> Response:
        try:
            document = Document.objects.get(pk=pk, owner=request.user)
            return Response(
                {"id": document.id, "status": document.status},
                status=status.HTTP_200_OK,
            )
        except Document.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
