# coding: utf-8
from django.urls import path
from .views import CreateJobOffer, \
    JobOfferDetailView, \
    UpdateJobOffer, \
    DeleteJobOffer
from . import views

urlpatterns = [
    path('',
         views.home, name='home'
         ),
    path('legal_notices',
         views.legal_notices,
         name='legal_notices'
         ),
    path('contact',
         views.contact,
         name='contact'
         ),
    path('see_categories',
         views.see_categories,
         name='see_categories'
         ),
    path('add_categories',
         views.add_category,
         name='add_categories'
         ),
    path('enter_category/<str:id_cat>/',
         views.enter_category,
         name='enter_category'
         ),
    path('delete_category/<str:cat_id>',
         views.delete_category,
         name='delete_category'
         ),
    path('job_description/<str:cate_id>',
         views.job_offers_views,
         name='job_description'
         ),
    path('job_detail/<int:pk>',
         JobOfferDetailView.as_view(),
         name='job_detail'
         ),
    path('add_job',
         CreateJobOffer.as_view(),
         name='add_job'
         ),
    path('job_detail/edit/<int:pk>',
         UpdateJobOffer.as_view(),
         name='update_job'
         ),
    path('job_detail/<int:pk>/delete',
         DeleteJobOffer.as_view(),
         name='delete_job'
         ),
    path('status/<str:status_id>/<str:catid>',
         views.select_status,
         name='status_select'
         )

]
