from django.contrib import admin
from django.urls import path, include
from setup.views import *
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()


urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/usuarios/', ListaUsuarios.as_view()),
    path('api/feed_geral/', ListarPosts.as_view()),
    path('api/feed_seguidores/', ListarPostsSeguidores.as_view()),
    path('api/seguidores/', ListarSeguidores.as_view()),
    path('api/seguir/<str:email>/', comecarSeguir, name="teste"),
    path('api/login/', signin),
    path('api/user_info/', user_info),
    path('api/cadastrar_usuario/', CreateUserView.as_view()),
    path('api/logout/', Logout.as_view()),
    path('api/criar_post/', CreatePostView.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
