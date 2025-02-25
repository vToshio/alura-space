from django import forms

class LoginForm(forms.Form):
    nome_login = forms.CharField(
        max_length=100,
        required=True,
        label='Nome de Usuário',
        widget=forms.TextInput(
            attrs = {
                'class': 'form-control text-dark',
                'placeholder': 'Nome de Usuário'
            }
        )
    )
    senha = forms.CharField(
        max_length=70,
        required=True,
        label='Senha',
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control text-dark',
                'placeholder': 'Senha'
            }
        )
    )

class CadastroForm(forms.Form):
    nome_cadastro = forms.CharField(
        required=True,
        max_length=100,
        label='Nome do Usuário',
        widget=forms.TextInput(
            attrs = {
                'class': 'form-control text-dark',
                'placeholder': 'Nome de Usuário'
            }
        )
    )
    email = forms.EmailField(
        max_length=100,
        required=True,
        label='Email',
        widget=forms.EmailInput(
            attrs = {
                'class': 'form-control text-dark',
                'placeholder': 'exemplo@email.com'
            }
        )
    )
    senha1 = forms.CharField(
        max_length=70,
        required=True,
        label='Senha',
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control text-dark',
                'placeholder': 'Senha'
            }
        )
    )
    senha2 = forms.CharField(
        max_length=70,
        required=True,
        label='Confirmar Senha',
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control text-dark',
                'placeholder': 'Confirmar Senha'
            }
        )
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')
        
        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Espaços não são permitidos nesse campo.')
            return nome
    

    def clean_senha2(self):
        senha1 = self.cleaned_data.get('senha1')
        senha2 = self.cleaned_data.get('senha2')

        if senha1 and senha2:
            if senha2 != senha1:
                raise forms.ValidationError('O campo de confirmação deve ser idêntico ao campo de senha.')
            return senha1