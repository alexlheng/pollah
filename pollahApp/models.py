from django.db import models

# Create your models here.

class pollah_question(models.Model):
	question_text = models.CharField(max_length=1023)
	time_created = models.DateTimeField('Time Created')
	def __str__(self):
		return self.question_text

class pollah_answer(models.Model):
	question = models.ForeignKey(pollah_question)
	answer_text = models.CharField(max_length=1023)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.answer_text