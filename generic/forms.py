from django.forms import (
    BooleanField,
    ModelForm,
)


class CustomForm(ModelForm):
    template_name = 'forms/default.html'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            print(type(visible.field))
            if type(visible.field) is BooleanField:
                visible.field.widget.attrs['class'] = 'form-check-input'
            else:
                visible.field.widget.attrs['class'] = 'form-control'
