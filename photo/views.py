from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,DetailView,DeleteView
from django.urls import reverse_lazy
from .forms import PhotoPostForm
from .models import PhotoPost

#ログイン状態でviewを呼び出すためのもの
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class IndexView(ListView):
    #index.htmlを指定する
    template_name = 'index.html'
    
    #モデルの指定
    #投稿日順に並び替える
    queryset = PhotoPost.objects.order_by('-posted_at')
    
    #1ページに表示するデータの数
    paginate_by = 9

@method_decorator(login_required, name='dispatch')
class CreatePhotoView(CreateView):
    form_class = PhotoPostForm
    #描画するhtmlファイル
    template_name = 'post_photo.html'
    #データ登録後に映るページ
    success_url = reverse_lazy('photo:post_done')
    #モデルに保存
    def form_valid(self,form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)
    
class PostSuccessView(TemplateView):
    template_name = 'post_success.html'
    
class CategoryView(ListView):
    template_name ='index.html'
    # paginate_by = 6
    def get_queryset(self):
        category_id =self.kwargs['category']
        records = PhotoPost.objects.filter(
            category=category_id).order_by('-posted_at')
        return records
    
class UserView(ListView):
    template_name ='index.html'
    # paginate_by = 6
    def get_queryset(self):
        user_id =self.kwargs['user']
        records = PhotoPost.objects.filter(
            user=user_id).order_by('-posted_at')
        return records
    
class PhotoDetailView(DetailView):
    template_name = 'detail.html'
    model = PhotoPost
    
class MypageView(ListView):
    template_name ='mypage.html'
    paginate_by = 6
    #ログインしているユーザーの投稿写真一覧を返す関数
    def get_queryset(self):
        records = PhotoPost.objects.filter(
            user=self.request.user).order_by('-posted_at')
        return records
    
class PhotoDeleteView(DeleteView):
    template_name = 'photo_delete.html'
    model = PhotoPost
    success_url = reverse_lazy('photo:mypage')