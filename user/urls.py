from django.urls import path , include
from rest_framework import routers
from user.views import UserViewSet
from .views1 import UserView, UserDetailView, UserUpdateView , UserDeleteView , UserCreateView
from .views2 import user_detail,user_view,user_create,user_update,user_delete
from .views3 import user_list,user_details , create_user , update_user ,delete_user

router = routers.DefaultRouter()
router.register('user', UserViewSet)

urlpatterns = [
    path('',include(router.urls)),

    path('users/',UserView.as_view(),name='users'),
    path('users/create', UserCreateView.as_view(), name='users_create'),
    path('users/<int:pk>',UserDetailView.as_view(),name='user_data'),
    path('users/<int:pk>/update',UserUpdateView.as_view(),name='user_update'),
    path('users/<int:pk>/delete', UserDeleteView.as_view(), name='user_delete'),

    path('fbv/users/',user_view,name='fbvusers'),
    path('fbv/users/create',user_create,name='fbvusercreate'),
    path('fbv/users/<int:pk>',user_detail,name='fbvuser'),
    path('fbv/users/<int:pk>/update',user_update,name='fbvuserupdate'),
    path('fbv/users/<int:pk>/delete',user_delete,name='fbvuserdelete'),

    path('api/users/',user_list),
    path('api/users/create',create_user),
    path('api/users/<int:pk>',user_details),
    path('api/users/<int:pk>/update',update_user),
    path('api/users/<int:pk>/delete',delete_user)
]

