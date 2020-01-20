from fcm_django.api.rest_framework import DeviceSerializerMixin
from fcm_django.models import FCMDevice
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from app.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

    def create(self, validate_data):
        us = Users.objects.filter(name=validate_data.get('name'))
        if 0 == len(us):
            users = Users(name=validate_data.get('name'),
                          login=validate_data.get('login'),
                          password=validate_data.get('password'),
                          avatar=validate_data.get('avatar'),
                          birth_date=validate_data.get('birth_date'),
                          place=validate_data.get('place'),
                          is_kg=validate_data.get('is_kg'),
                          is_ru=validate_data.get('is_ru'),
                          )
            users.save()
            return users
        else:
            return us[0]


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class RatingAllSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Rating
        fields = '__all__'


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'


class GameQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameQuiz
        fields = '__all__'


class GameQuizGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameQuizGame
        fields = '__all__'


class GameQuizGameSerializerGandon(serializers.ModelSerializer):
    user_owner = UserSerializer()
    user_outer = UserSerializer()

    class Meta:
        model = GameQuizGame
        fields = '__all__'


class MainCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCategory
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class DayQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayQuiz
        fields = '__all__'


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'


class CountSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizCount
        fields = '__all__'


class UniversitySubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversitySubCategory
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class OrtSerializer(serializers.ModelSerializer):
    class Meta:
        model = ORT
        fields = '__all__'


class OrtDescSerializer(serializers.ModelSerializer):
    class Meta:
        model = ORTDesc
        fields = '__all__'


class FCMDeviceSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data['users'])

        if not Device.objects.filter(users=validated_data['users']).exists():
            new_instance = Device(registration_id=validated_data['registration_id'],
                                  type='android',
                                  users=validated_data['users'])
            new_instance.save()
            return new_instance

        instance = Device.objects.get(users=validated_data['users'])
        instance.registration_id = validated_data['registration_id']
        instance.save()

        return instance


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'


class AnswerQuizSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = AnswerToComment
        fields = '__all__'


class CommentQuizSerializer(serializers.ModelSerializer):
    answer = AnswerQuizSerializer(many=True)
    user = UserSerializer()

    class Meta:
        model = CommentQuestion
        fields = 'id,answer,name,message,quiz,user'.split(',')

    def get_answers(self, obj):
        return AnswerQuizSerializer(obj.answer).data


class CommentQuizCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentQuestion
        fields = '__all__'


class AnswerQuizCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnswerToComment
        fields = '__all__'