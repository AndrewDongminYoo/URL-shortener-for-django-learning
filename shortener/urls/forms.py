from django import forms
from django.utils.translation import gettext_lazy as _
from shortener.models import ShortenedUrls
from shortener.users.utils import url_count_changer


class UrlCreateForm(forms.ModelForm):
    class Meta:
        model = ShortenedUrls
        fields = ["nick_name", "target_url"]
        labels = {
            "nick_name": _("별칭"),
            "target_url": _("URL"),
        }
        widgets = {
            "nick_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "URL을 구분하기 위한 별칭"}),
            "target_url": forms.TextInput(attrs={"class": "form-control", "placeholder": "포워딩될 URL"}),
        }

    def save_form(self, request, commit=True):
        instance = super(UrlCreateForm, self).save(commit=False)
        instance.creator_id = request.user.id
        instance.target_url = instance.target_url.strip()
        if commit:
            try:
                instance.save()
            except Exception as e:
                print("Error detected:: forms.py 28 lines", e)
            else:
                url_count_changer(request=request, is_increase=True)
        return instance

    def update_form(self, request, url_id):
        instance = super(UrlCreateForm, self).save(commit=False)
        instance.target_url = instance.target_url.strip()
        ShortenedUrls.objects.filter(pk=url_id, creator_id=request.user.id).update(
            target_url=instance.target_url, nick_name=instance.nick_name
        )
