import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
# definir como os dados serão tratados e vai cuspir a informação para o banco de dados

class Question(models.Model):
    question_text = models.CharField(max_length=200) # campo de caracters
    pub_date = models.DateTimeField('date_published')

    def __str__(self):
        return f"{self.question_text}"
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # toda alternativa tem que estar vinculada a uma pergunta
    # toda pergunta tem que ter um ID, ele vai fazer a relação entre as tabelas
    # se eu apagar a pergunta, vai apagar as alternativas também
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) # começa em 0

    def __str__(self):
        return f"{self.choice_text}"