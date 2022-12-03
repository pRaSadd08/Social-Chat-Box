from django.urls import path
from.import views

urlpatterns=[
    path ('',views.chat, name='chat'),
    path ('delete/<int:id>',views.delete, name='delete'),
    path ('edit/<int:id>',views.edit, name="edit"),
    path ('like/<int:post_id>/',views.LikeView,name='like'),
    # path ('upload/<int:post_id>/',views.upload,name='upload')
] 