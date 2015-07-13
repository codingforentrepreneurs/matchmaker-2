from django import forms

LEVELS = (
		('Mandatory', 'Mandatory'), 
		('Very Important', 'Very Important'),
		('Somewhat Important', 'Somewhat Important'),
		('Not Important','Not Important'),
		)

class UserResponseForm(forms.Form):
	question_id = forms.IntegerField()
	answer_id = forms.IntegerField()
	importance_level = forms.ChoiceField(choices=LEVELS)
	coworker_answer_id = forms.IntegerField()
	coworker_importance_level = forms.ChoiceField(choices=LEVELS)
