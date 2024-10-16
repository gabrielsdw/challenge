from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LessonModelSerializer
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsOwnerOrReadOnly
from .models import Lesson


class LessonApiView(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def post(self, request, pk):
        # Obtém a lição pelo ID.
        lesson = get_object_or_404(Lesson, pk=pk)
        
        # Cria o serializer com os dados recebidos na requisição.
        serializer = LessonModelSerializer(data=request.data)
       
        if serializer.is_valid():
            # Obtém o novo conteúdo HTML da requisição.
            new_html_content = serializer.validated_data.get('html_content', None)
            
            if new_html_content is not None:
                # Pega o conteúdo HTML antigo da lição.
                old_html_content = lesson.html_content

                # Combina o conteúdo antigo com o novo.
                combined_html_content = old_html_content + new_html_content

                # Atualiza o campo html_content da lição.
                lesson.html_content = combined_html_content
                lesson.save()

                # Retorna o conteúdo combinado na resposta.
                return Response(
                    {'html_content': combined_html_content},
                    status=status.HTTP_200_OK
                )
        
        # Retorna erros de validação, se existirem.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
