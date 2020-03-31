from django.contrib import admin

# Register your models here.
from django import forms
from django.contrib.admin import StackedInline
from django_summernote.widgets import SummernoteWidget
from jet.admin import CompactInline

from app.models import *

admin.site.register(MainCategory)
admin.site.register(Category)
admin.site.register(GameQuizGame)
admin.site.register(Notification)
admin.site.register(Device)
admin.site.register(Quote)
admin.site.register(MyNotif)
admin.site.register(CommentQuestion)
admin.site.register(AnswerToComment)
admin.site.register(LikeQuiz)
admin.site.register(LikeAnswerQuiz)
admin.site.register(LikeAnswerForum)
admin.site.register(LikeForum)


class UsersAdmin(admin.ModelAdmin):
    model = Users
    search_fields = ('name',)
    list_display = ("name", "login")


admin.site.register(Users, UsersAdmin)


class InfoAdminForm(forms.ModelForm):
    class Meta:
        model = Info
        widgets = {
            'desc': SummernoteWidget(),
        }
        fields = '__all__'


class InfoAdmin(admin.ModelAdmin):
    form = InfoAdminForm
    model = Info


admin.site.register(Info, InfoAdmin)


class UniversitySubCategoryAdminForm(forms.ModelForm):
    class Meta:
        model = UniversitySubCategory
        widgets = {
            'desc': SummernoteWidget(),
        }
        fields = '__all__'


class UniversitySubcategoryAdmin(CompactInline):
    form = UniversitySubCategoryAdminForm
    model = UniversitySubCategory
    extra = 1


class UniversityAdminForm(forms.ModelForm):
    class Meta:
        model = University
        widgets = {
            'desc': SummernoteWidget(),
        }
        fields = '__all__'


class UniversityAdmin(admin.ModelAdmin):
    form = UniversityAdminForm
    model = University
    inlines = [UniversitySubcategoryAdmin]


admin.site.register(University, UniversityAdmin)


class DayQuizAdminForm(forms.ModelForm):
    class Meta:
        model = DayQuiz
        widgets = {
            'question': SummernoteWidget(),
            'answer_a': SummernoteWidget(),
            'answer_b': SummernoteWidget(),
            'answer_c': SummernoteWidget(),
            'answer_d': SummernoteWidget(),
            'answer_e': SummernoteWidget(),
        }
        fields = '__all__'


class DayQuizAdmin(admin.ModelAdmin):
    form = DayQuizAdminForm
    model = DayQuiz


admin.site.register(DayQuiz, DayQuizAdmin)


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Quiz
        widgets = {
            'question': SummernoteWidget(),
            'answer_a': SummernoteWidget(),
            'answer_b': SummernoteWidget(),
            'answer_c': SummernoteWidget(),
            'answer_d': SummernoteWidget(),
            'answer_e': SummernoteWidget(),

        }
        fields = '__all__'


class QuizAdmin(CompactInline):
    form = PostAdminForm
    model = Quiz
    extra = 1


class TestAdminForm(forms.ModelForm):
    class Meta:
        model = Test
        widgets = {
            'desc': SummernoteWidget(),
        }
        fields = '__all__'


class TestAdmin(admin.ModelAdmin):
    form = TestAdminForm
    ordering = ['name']
    list_filter = ['category', ]

    class Meta:
        model = Test

    list_display = ("name", "display_category_name")

    inlines = [QuizAdmin]

    def display_category_name(self, obj):
        return obj.category.name


admin.site.register(Test, TestAdmin)


class GameQuizAdminForm(forms.ModelForm):
    class Meta:
        model = GameQuiz
        widgets = {
            'question': SummernoteWidget(),
            'answer_a': SummernoteWidget(),
            'answer_b': SummernoteWidget(),
            'answer_c': SummernoteWidget(),
            'answer_d': SummernoteWidget(),
            'answer_e': SummernoteWidget(),
        }
        fields = '__all__'


class GameQuizAdmin(admin.ModelAdmin):
    form = GameQuizAdminForm
    model = GameQuiz
    search_fields = ('question',)


admin.site.register(GameQuiz, GameQuizAdmin)


class GameTestAdmin(admin.ModelAdmin):
    class Meta:
        model = Game


admin.site.register(Game, GameTestAdmin)


class OrtDescAdminForm(forms.ModelForm):
    class Meta:
        model = ORTDesc
        widgets = {
            'desc': SummernoteWidget(),
        }
        fields = '__all__'


class ORTDescAdmin(admin.ModelAdmin):
    form = OrtDescAdminForm
    model = ORTDesc


admin.site.register(ORTDesc, ORTDescAdmin)


class OrtAdmin(admin.ModelAdmin):
    model = ORT
    # inlines = [ORTDescAdmin]


admin.site.register(ORT, OrtAdmin)


class NewsAdminForm(forms.ModelForm):
    class Meta:
        model = News
        widgets = {
            'desc': SummernoteWidget(),
        }
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    model = News


admin.site.register(News, NewsAdmin)


class RatingAdmin(admin.ModelAdmin):
    ordering = ['user']
    list_filter = ['user', ]

    class Meta:
        model = Rating

    list_display = ('rating', 'created_at')


admin.site.register(Rating, RatingAdmin)


class ForumAdmin(admin.ModelAdmin):

    class Meta:
        model = Forum

    list_display = ('title', 'created_at', 'lang')


admin.site.register(Forum, ForumAdmin)


class TopicAdmin(admin.ModelAdmin):

    class Meta:
        model = Topic1

    list_display = ('title', 'created_at', 'display_forum_title')

    def display_forum_title(self, obj):
        return obj.forum.title


admin.site.register(Topic1, TopicAdmin)


class CommentForumAdmin(admin.ModelAdmin):
    search_fields = ['message', ]

    class Meta:
        model = CommentForum

    list_display = ("message", "display_user_name", 'created_at')

    def display_user_name(self, obj):
        return obj.user.name


admin.site.register(CommentForum, CommentForumAdmin)


class AnswerForumAdmin(admin.ModelAdmin):
    search_fields = ['message', ]

    class Meta:
        model = AnswerToCommentForum

    list_display = ("message", "display_user_name", 'created_at')

    def display_user_name(self, obj):
        return obj.user.name


admin.site.register(AnswerToCommentForum, AnswerForumAdmin)