from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, label='이메일')
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'username': '사용자명',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = '비밀번호'
        self.fields['password2'].label = '비밀번호 확인'

class ProfileUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='이메일')
    
    class Meta:
        model = User
        fields = ('email',)

def signup(request):
    """회원가입"""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '회원가입이 완료되었습니다.')
            return redirect('medicine:index')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    """로그인"""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'{username}님, 환영합니다!')
                return redirect('medicine:index')
        else:
            messages.error(request, '아이디 또는 비밀번호가 올바르지 않습니다.')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    """로그아웃"""
    logout(request)
    messages.info(request, '로그아웃되었습니다.')
    return redirect('medicine:index')

@login_required
def profile(request):
    """회원정보 수정"""
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        password_form = PasswordChangeForm(request.user, request.POST)
        
        # 이메일 수정
        if 'update_email' in request.POST and form.is_valid():
            form.save()
            messages.success(request, '이메일이 수정되었습니다.')
            return redirect('accounts:profile')
        
        # 비밀번호 수정
        if 'change_password' in request.POST and password_form.is_valid():
            user = password_form.save()
            login(request, user)  # 비밀번호 변경 후 세션 유지
            messages.success(request, '비밀번호가 수정되었습니다.')
            return redirect('accounts:profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
        password_form = PasswordChangeForm(request.user)
    
    return render(request, 'accounts/profile.html', {
        'form': form,
        'password_form': password_form
    })

