from django.contrib import admin

# Register your models here.
from django import forms
from django_summernote.widgets import SummernoteWidget
from jet.admin import CompactInline

from app.models import *

admin.site.register(Users)
admin.site.register(MainCategory)
admin.site.register(Category)
admin.site.register(Rating)
admin.site.register(GameQuizGame)
admin.site.register(Notification)
admin.site.register(Device)


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


class TestAdmin(admin.ModelAdmin):
    class Meta:
        model = Test

    inlines = [QuizAdmin]


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


class GameQuizAdmin(CompactInline):
    form = GameQuizAdminForm
    model = GameQuiz
    extra = 1


class GameTestAdmin(admin.ModelAdmin):
    class Meta:
        model = Game

    inlines = [GameQuizAdmin]


admin.site.register(Game, GameTestAdmin)


class OrtDescAdminForm(forms.ModelForm):
    class Meta:
        model = ORTDesc
        widgets = {
            'desc': SummernoteWidget(),
        }
        fields = '__all__'


class ORTDescAdmin(CompactInline):
    form = OrtDescAdminForm
    model = ORTDesc
    extra = 1


class OrtAdmin(admin.ModelAdmin):
    model = ORT
    inlines = [ORTDescAdmin]


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

