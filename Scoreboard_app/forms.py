from django import forms  
from Scoreboard_app.models import Scores
class ScoresForm(forms.ModelForm):  #Form for new player input, used in views.py emp def which adds new player to database.
    class Meta:  
        model = Scores 
        fields = "__all__"  