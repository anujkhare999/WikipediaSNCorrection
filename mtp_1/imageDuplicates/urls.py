from django.urls import path
from . import views
app_name = 'imageDuplicates'

urlpatterns=[
    # # ex: /polls/
    # path('',views.index, name='index'),
    # # ex: /polls/5/
    # path('<int:question_id>/',views.detail,name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/',views.results,name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/',views.vote,name='vote'),

    path('',views.IndexView.as_view(),name='index2'),
    path('<int:pk>',views.DetailView,name='detail'),
    path('vote/<int:pk1>/<int:pk2>',views.VoteView,name='vote'),
    # path('<int:pk>/results/',views.ResultsView.as_view(),name='results'),
    # path('<int:question_id>/vote/',views.vote,name='vote'),
    path('search/',views.search,name='search'),
]