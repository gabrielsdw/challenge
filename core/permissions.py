from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    """
    Permite que apenas o proprietário (usuário autenticado) possa editar ou deletar seus próprios dados.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        print(bool(obj == request.user))
        return bool(obj == request.user)