from django.db import models

#accountsアプリのCustomUserモデルをインポート
from accounts.models import CustomUser

#投稿する写真のカテゴリ
class Category(models.Model):
    title = models.CharField(
            verbose_name = 'カテゴリ',
            max_length = 20)
    
    def __str__(self):
        return self.title
    
#投稿されたデータを管理するためのモデル
class PhotoPost(models.Model):
    #ユーザー名
    user = models.ForeignKey(
        CustomUser,
        verbose_name = 'ユーザー',
        #ユーザーを削除すると投稿データも連動して削除する処理
        on_delete = models.CASCADE)
    
    #カテゴリ
    category = models.ForeignKey(
                    Category,
                    verbose_name = 'カテゴリ',
                    on_delete = models.PROTECT)
    
    #タイトル
    title = models.CharField(
                verbose_name = 'タイトル',
                max_length = 200)
    
    #コメント
    comment = models.TextField(
                    verbose_name = 'コメント')
    
    #画像1
    image1 = models.ImageField(
            verbose_name = 'イメージ１',
            #ファイルの保存先フォルダ名
            upload_to = 'photos')
    
    #画像2
    image2 = models.ImageField(
            verbose_name = 'イメージ2',
            #ファイルの保存先フォルダ名
            upload_to = 'photos',
            #画像２はなくても良い
            blank = True,
            null = True)
    
    #投稿日時
    posted_at = models.DateTimeField(
                    verbose_name = '投稿日時',
                    auto_now_add = True)
    #表示をカテゴリ名にするための処理
    def __str__(self):
        return self.title