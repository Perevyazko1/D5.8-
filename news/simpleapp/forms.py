from django import forms
from django.core.exceptions import ValidationError

from .models import News


class NewsForm(forms.ModelForm):
    # description = forms.CharField(min_length=20)

    class Meta:
        model = News
        fields = [
            'title',
            'text',
            'category'

        ]

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("title")
        # description = cleaned_data.get("text")
        #
        # if description is not None and len(description) < 20:
        #     raise ValidationError({
        #         "description": "Описание не может быть менее 20 символов."
        #     })
        #
        # if name == description:
        #     raise ValidationError(
        #         "Описание не должно быть идентично названию."
        #     )

        return cleaned_data