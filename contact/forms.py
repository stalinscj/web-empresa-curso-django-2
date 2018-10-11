from django import forms

class ContactForm(forms.Form):
	name = forms.CharField(label='Nombre', required=True, min_length=3, max_length=100, widget=forms.TextInput(
		attrs = {
			'class' : 'form-control',
			'placeholder' : 'Escribe tu Nombre',
		}
	))
	email = forms.EmailField(label='Email', required=True, min_length=3, max_length=100, widget=forms.EmailInput(
		attrs = {
			'class' : 'form-control',
			'placeholder' : 'Escribe tu Email',
		}
	))
	content = forms.CharField(label='Mensaje', required=True, min_length=10, max_length=1000, widget=forms.Textarea(
		attrs = {
			'class' : 'form-control',
			'placeholder' : 'Escribe tu Mensaje',
			'rows' : 3,
		}
	))
		