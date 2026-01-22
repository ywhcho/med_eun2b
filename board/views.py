from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import F
from .models import Post
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        labels = {
            'title': '제목',
            'content': '내용',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }

def post_list(request):
    """게시글 목록"""
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)  # 10개씩 페이징
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'board/list.html', {'page_obj': page_obj})

def post_detail(request, pk):
    """게시글 상세보기"""
    post = get_object_or_404(Post, pk=pk)
    
    # 조회수 증가 (F 표현식 사용하여 race condition 방지)
    Post.objects.filter(pk=pk).update(views=F('views') + 1)
    post.refresh_from_db()
    
    return render(request, 'board/detail.html', {'post': post})

@login_required
def post_create(request):
    """게시글 작성"""
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, '게시글이 작성되었습니다.')
            return redirect('board:detail', pk=post.pk)
    else:
        form = PostForm()
    
    return render(request, 'board/form.html', {'form': form, 'title': '게시글 작성'})

@login_required
def post_edit(request, pk):
    """게시글 수정"""
    post = get_object_or_404(Post, pk=pk)
    
    # 작성자 확인
    if post.author != request.user:
        messages.error(request, '수정 권한이 없습니다.')
        return redirect('board:detail', pk=pk)
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, '게시글이 수정되었습니다.')
            return redirect('board:detail', pk=pk)
    else:
        form = PostForm(instance=post)
    
    return render(request, 'board/form.html', {'form': form, 'title': '게시글 수정'})

@login_required
def post_delete(request, pk):
    """게시글 삭제"""
    post = get_object_or_404(Post, pk=pk)
    
    # 작성자 확인
    if post.author != request.user:
        messages.error(request, '삭제 권한이 없습니다.')
        return redirect('board:detail', pk=pk)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, '게시글이 삭제되었습니다.')
        return redirect('board:list')
    
    return render(request, 'board/delete.html', {'post': post})

