from django import forms

from .models import LEVELS

class UserResponseForm(forms.Form):
	question_id = forms.IntegerField()
	answer_id = forms.IntegerField()
	importance_level = forms.ChoiceField(choices=LEVELS)
	their_answer_id = forms.IntegerField()
	their_importance_level = forms.ChoiceField(choices=LEVELS)
