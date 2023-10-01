from django import forms

from dropdownlist.models import Branch, Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset = Branch.objects.none()

        if 'collage' in self.data:
            try:
                collage_id = int(self.data.get('collage'))
                self.fields['branch'].queryset = Branch.objects.filter(collage_id=collage_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['branch'].queryset = self.instance.collage.branch_set.order_by('name')