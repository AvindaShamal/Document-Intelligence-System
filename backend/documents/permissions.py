from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Custom permission to only allow owners of a document to access it.
    """

    def has_object_permission(self, request, view, obj) -> bool:
        # Object-level permission to only allow owners of the document to access it
        return obj.owner == request.user
