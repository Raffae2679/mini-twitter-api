from rest_framework import viewsets, generics,parsers
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from setup.models import Usuario, Post
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from setup.serializer import UsuarioSerializer, PostSerializer, UserSigninSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from django.contrib.auth import authenticate
from .Authentication import token_expire_handler, expires_in


    
# Listar Usuarios
class ListaUsuarios(generics.ListAPIView):

    def get_queryset(self):
        
        queryset = Usuario.objects.all()
        return queryset
    serializer_class = UsuarioSerializer
    

# Listar Posts
class ListarPosts(generics.ListAPIView):

    def get_queryset(self):
        queryset = Post.objects.all().exclude(autor=self.request.user)
        
        return queryset
    
    serializer_class = PostSerializer
    

@api_view(('POST',))
def comecarSeguir(request, email):
    
    user = request.user
    user_seguido = Usuario.objects.get(email=email)
        
    user.seguidores.add(user_seguido)
    user.save()


    content = {'Sucesso': 'Usuário adicionado a lista de seguindo'}
    return Response(content,status=status.HTTP_200_OK)
    
    
# Listar Seguidore
class ListarSeguidores(generics.ListAPIView):

    def get_queryset(self):
        queryset = self.request.user.seguidores
        return queryset
    
    serializer_class = UsuarioSerializer
    
    
# Listar Posts dos Seguidores
class ListarPostsSeguidores(generics.ListAPIView):

    def get_queryset(self):
        seguidores = self.request.user.seguidores.all()
        
        
        queryset = Post.objects.filter(autor__in=seguidores)
        print(queryset)
        
        return queryset
    
    serializer_class = PostSerializer


    
@api_view(["POST"])
@permission_classes((AllowAny,))  # Setado a permissão para acesso 
def signin(request):
    signin_serializer = UserSigninSerializer(data = request.data)
    if not signin_serializer.is_valid():
        return Response(signin_serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    user = authenticate(
            username = signin_serializer.data['username'],
            password = signin_serializer.data['password'] 
        )
    if not user:
        return Response({'detail': 'Invalid Credentials or activate account'}, status=status.HTTP_404_NOT_FOUND)
        
    token, _ = Token.objects.get_or_create(user = user)
    
    # Irá verificar o token, se expirado, criara outro
    is_expired, token = token_expire_handler(token)     
    user_serialized = UsuarioSerializer(user)

    return Response({
        'user': user_serialized.data, 
        'expires_in': expires_in(token),
        'token': token.key
    }, status=status.HTTP_200_OK)


# Informações do usuario, token e ID
@api_view(["GET"])
def user_info(request):
    return Response({
        'id': request.user.id,
        'user': request.user.username,
        'expires_in': expires_in(request.auth)
    }, status=status.HTTP_200_OK)

# Responsavel por criar um novo usuário
class CreateUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = UsuarioSerializer

# Responsável pelo logou
class Logout(APIView):
    def get(self, request, format=None):
        # Apaga o token ativo
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

# Criar post
class CreatePostView(CreateAPIView):
    model = Post
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    serializer_class = PostSerializer