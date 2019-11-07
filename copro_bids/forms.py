from django import forms
from .models import Project, Bid, Teammate


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('client', 'code', 'name', 'bid_deadline')


class BidForm(forms.ModelForm):

    class Meta:
        model = Bid
        fields = ('project', 'name', 'email', 'phases_and_pricing', 'total_price',
                  'website_urls', 'work_sample_urls', 'statement', 'conditions')


class TeammateForm(forms.ModelForm):

    class Meta:
        model = Teammate
        fields = ('bid', 'first_name', 'last_name', 'img_url', 'role',
                  'years_experience', 'city', 'state', 'country', 'public_profile_urls')
