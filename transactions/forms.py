from django.forms import FileField, ModelForm

from .models import Transaction


class TransactionForm(ModelForm):
    file = FileField()

    class Meta:
        model = Transaction
        fields = ["file"]


file = TransactionForm.base_fields["file"]
file.widget.attrs["accept"] = ".txt"
