from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnlyUser(BasePermission):
    """
    Permite que apenas o proprietário (usuário autenticado) possa editar ou deletar seus próprios dados.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return bool(obj == request.user)
    

class IsOwnerOrReadOnlyLesson(BasePermission):
    """
    Permite que apenas o proprietário (usuário autenticado) possa editar ou deletar seus próprios dados.
    """

    def has_object_permission(self, request, view, obj):
        print(request.user)
        if request.method in SAFE_METHODS:
            return True
        return bool(obj.user == request.user)