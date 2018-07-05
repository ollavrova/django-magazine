from django import forms


class SignupForm(forms.Form):
    email = forms.EmailField()
    role = forms.IntegerField(min_value=1, max_value=3)
    birth_date = forms.DateField()
    password1 = forms.CharField(max_length=254, label='Password1', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=254, label='Password2', widget=forms.PasswordInput)

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.last_name = self.cleaned_data['last_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        models.Profile(
            user=user,
            phone=self.cleaned_data['phone'],
         ).save()


    def signup(self, request, user):
        # I believe allauth has already created the user, and now it's passing it to this so you can do any final touches to it, like profile stuff. I could be wrong.
        summoner_id = self.cleaned_data.get('summoner_id')
        summoner_name = self.cleaned_data.get('summoner_name')
        if not hasattr(user,
                       'userprofile'):  # probably not necessary, but this is how you check if a user.userprofile exists easily
            UserProfile.objects.create(user=user, summoner_id=summoner_id, summoner_name=summoner_name)
        return user