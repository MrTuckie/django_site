from django.urls import path
from . import views # traz tudo que tá na views

app_name = 'polls'

# falta incluir no projeto agora
urlpatterns = [
    path('',views.index, name='index'),
    path('<int:question_id>/results/',views.results, name='results'),
    path('<int:question_id>/vote',views.vote, name='vote'),
]