"""Quizz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from app import views
from app.views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'users_duel', UsersForDuelViewSet)
router.register(r'tests', TestViewSet)
router.register(r'quiz', QuizViewSet)
router.register(r'rating', RatingViewSet)
router.register(r'game', GameViewSet)
router.register(r'game_cache', GameQuizGameViewSet)
router.register(r'main_category', MainCategoryViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'day_quiz', DayQuizViewSet)
router.register(r'info', InfoViewSet)
router.register(r'university', UniversityViewSet)
router.register(r'university_sub', UniversitySubCategoryViewSet)
router.register(r'count', CountViewSet)
router.register(r'news', NewsViewSet)
router.register(r'ort', OrtViewSet)
router.register(r'rating_all_of', RatingAllViewSet)
router.register(r'rating_all_of_pagination', RatingAllWithPaginationViewSet)
router.register(r'ort_desc', OrtDescViewSet)
router.register(r'notification', NotificationViewSet)
router.register(r'comment_quiz', CommentQuizViewSet)
router.register(r'comment_quiz_create', CommentQuizCreateViewSet)
router.register(r'answer_quiz', AnswerQuizViewSet)
router.register(r'like_quiz', LikeQuizViewSet)
router.register(r'like_answer_quiz', LikeAnswerQuizViewSet)
router.register(r'comment_forum', CommentForumViewSet)
router.register(r'comment_forum_create', CommentForumCreateViewSet)
router.register(r'answer_forum', AnswerForumViewSet)
router.register(r'like_forum', LikeForumViewSet)
router.register(r'like_answer_forum', LikeAnswerForumViewSet)
router.register(r'friend', FriendViewSet)
router.register(r'my_friend', MyFriendViewSet)
router.register(r'search_users', SearchUsersForDuelViewSet)
router.register(r'forum', ForumViewSet)
router.register(r'topic', TopicViewSet)
router.register(r'topic_create', TopicCreateViewSet)
router.register(r'math1', Math1OrtViewSet)
router.register(r'math2', Math2OrtViewSet)
router.register(r'analog', AnalogOrtViewSet)
router.register(r'understand', UnderstandOrtViewSet)
router.register(r'grammar', GrammarOrtViewSet)
router.register(r'pay', PayOrtViewSet)
router.register(r'point_ort', PointsOrtOrtViewSet)
router.register(r'point_ort_get', PointsOrtOrtGetViewSet)
router.register(r'category_ort', CategoryOrtViewSet)
router.register(r'desc_ort', DescOrtViewSet)
router.register(r'pay_info', PayInfoViewSet)
urlpatterns = [
                  url(r'^jet/', include('jet.urls', 'jet')),
                  url(r'^summernote/', include('django_summernote.urls')),
                  path('admin/', admin.site.urls),
                  path('api/v1/', include(router.urls)),
                  path('api/v1/game_quiz/', views.game_quiz_list),
                  path('api/v1/rating_al/', RatingAll.as_view()),
                  path('api/v1/rating_first/', RatingFirst.as_view()),
                  path('api/v1/is_exist/', IsUserExist.as_view()),
                  path('api/v1/game_all/', GameInviteAll.as_view()),
                  path('api/v1/category_lang/', Category1.as_view()),
                  path('api/v1/delete/', DeleteSultan.as_view()),
                  path('api/v1/quote/', QuoteG.as_view()),
                  path('api/v1/game_lang/', Game1.as_view()),
                  path('api/v1/game_invite/', GameAll.as_view()),
                  path('api/v1/notification_count/', NotificationCount.as_view()),
                  path('api/v1/game_quiz_outer/', views.game_quiz_list_outer),
                  path('api/v1/device', FCMDeviceCreateView.as_view({'post': 'create'})),

                  # path('api/v1/rating_add/', views.set_rating),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
