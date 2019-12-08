from django.db import models

# Create your models here.
from fcm_django.models import FCMDevice


def image_upload_to(instance, filename):
    return "images/%s" % (filename)


LANG_CHOICES = ((1, 'KG'), (2, 'RU'))


class Users(models.Model):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    name = models.CharField(max_length=100, null=True, blank=True, verbose_name='ФИО')
    login = models.CharField(max_length=100, null=True, blank=True, verbose_name='логин')
    password = models.CharField(max_length=100, null=True, blank=True, verbose_name='пароль')
    avatar = models.ImageField(upload_to=image_upload_to, null=True, blank=True, verbose_name='аватар')
    birth_date = models.DateField(null=True, blank=True, verbose_name="дата рождения")
    place = models.CharField(null=True, blank=True, verbose_name="место проживания", max_length=100)
    duel_time = models.DateTimeField(auto_now=True, null=True)
    is_kg = models.BooleanField(null=True, blank=True, default=False)
    is_ru = models.BooleanField(null=True, blank=True, default=False)
    is_notification = models.BooleanField(null=True, blank=True, default=True)

    # rating = models.IntegerField(max_length=100, null=True, blank=True, verbose_name='рейтинг')

    def __str__(self):
        return self.name


class Test(models.Model):
    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

    lang = models.IntegerField(choices=LANG_CHOICES, null=True, blank=True)
    category = models.ForeignKey('Category', verbose_name='Категория', related_name='test',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=1000, null=True, blank=True, verbose_name='название')
    desc = models.TextField(null=True, blank=True, verbose_name='описание')


class Quiz(models.Model):
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    test = models.ForeignKey('Test', verbose_name='Тест', related_name='test',
                             on_delete=models.CASCADE)
    question = models.TextField(null=True, blank=True, verbose_name='вопрос')
    answer_a = models.TextField(null=True, blank=True, verbose_name='ответ_а')
    answer_b = models.TextField(null=True, blank=True, verbose_name='ответ_б')
    answer_c = models.TextField(null=True, blank=True, verbose_name='ответ_в')
    answer_d = models.TextField(null=True, blank=True, verbose_name='ответ_г')
    answer_e = models.TextField(null=True, blank=True, verbose_name='ответ_д')
    true_answer = models.CharField(max_length=1, verbose_name="правильный ответ")
    duration = models.IntegerField(null=True, blank=True, verbose_name='время одного вопроса')

    def __str__(self):
        return self.question


class Rating(models.Model):
    class Meta:
        verbose_name = 'рейтинг'
        verbose_name_plural = 'рейтинги'

    user = models.ForeignKey('Users', verbose_name='Пользователь', related_name='user',
                             on_delete=models.CASCADE)
    rating = models.IntegerField(verbose_name='рейтинг')
    created_at = models.CharField(null=True, blank=True, max_length=30)
    true_answer = models.IntegerField(null=True, blank=True, default=0)
    false_answer = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return str(self.rating)


class MainCategory(models.Model):
    class Meta:
        verbose_name = 'Главная Категория'
        verbose_name_plural = 'Главные Категории'

    lang = models.IntegerField(choices=LANG_CHOICES, null=True, blank=True)
    name = models.CharField(max_length=1000, null=True, blank=True, verbose_name='название')
    desc = models.TextField(null=True, blank=True, verbose_name='описание')
    image = models.ImageField(upload_to=image_upload_to, null=True, blank=True, verbose_name='логотип')

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    main_category = models.ForeignKey(MainCategory, verbose_name='главная категория', related_name='category',
                                      on_delete=models.CASCADE)
    lang = models.IntegerField(choices=LANG_CHOICES, null=True, blank=True)
    name = models.CharField(max_length=1000, null=True, blank=True, verbose_name='название')
    desc = models.CharField(max_length=1000, null=True, blank=True, verbose_name='описание')

    def __str__(self):
        return self.name


class Info(models.Model):
    class Meta:
        verbose_name = 'Инфо'
        verbose_name_plural = 'Инфо'

    main_category = models.ForeignKey(MainCategory, verbose_name='главная категория', related_name='info',
                                      on_delete=models.CASCADE)
    lang = models.IntegerField(choices=LANG_CHOICES, null=True, blank=True)
    name = models.TextField(verbose_name='Название')
    desc = models.TextField(verbose_name='Информация')

    def __str__(self):
        return self.main_category.name


class University(models.Model):
    class Meta:
        verbose_name = 'Вуз'
        verbose_name_plural = 'Вузы'

    lang = models.IntegerField(choices=LANG_CHOICES, null=True, blank=True)
    name = models.CharField(max_length=1000, verbose_name='Название')
    desc = models.TextField(verbose_name='Информация')
    avatar = models.ImageField(upload_to=image_upload_to, null=True, blank=True, verbose_name='логотип')

    def __str__(self):
        return self.name


class UniversitySubCategory(models.Model):
    class Meta:
        verbose_name = 'описание'
        verbose_name_plural = 'описание'

    university = models.ForeignKey(University, verbose_name='Универ', related_name='info',
                                   on_delete=models.CASCADE)
    name = models.CharField(max_length=1000, verbose_name='Название')
    desc = models.TextField(verbose_name='Информация')

    def __str__(self):
        return self.name


class ORT(models.Model):
    class Meta:
        verbose_name = 'Подготовка к ОРТ'
        verbose_name_plural = 'Подготовка к ОРТ'

    lang = models.IntegerField(choices=LANG_CHOICES, null=True, blank=True)
    name = models.CharField(max_length=1000, verbose_name='Название')

    def __str__(self):
        return self.name


class ORTDesc(models.Model):
    class Meta:
        verbose_name = 'Подготовка к ОРТ описание'
        verbose_name_plural = 'Подготовка к ОРТ описание'

    ort = models.ForeignKey(ORT, verbose_name='Орт', related_name='info',
                            on_delete=models.CASCADE)
    name = models.CharField(max_length=1000, verbose_name='Название')
    desc = models.TextField(verbose_name='Информация')

    def __str__(self):
        return self.name


class News(models.Model):
    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

    lang = models.IntegerField(choices=LANG_CHOICES, null=True, blank=True)
    name = models.CharField(max_length=1000, verbose_name='Название')
    desc = models.TextField(verbose_name='Информация')
    created_at = models.DateTimeField(null=True, blank=True, auto_now=True)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()
        users = Users.objects.all()

        for user in users:
            Notification(news=self, user=user, title="Новости/Жаңылыктар", body=self.name).save()
            if user.is_notification is None or user.is_notification is True:

                Device.objects.filter(users=user).send_message(
                    api_key="AAAA0w0fEAM:APA91bHCgAJUjQnWUMjBQFUrX8tbnhwTkNzw8RoLEMMMxZhTmDmayy2TQnPz3v26t7Y051wXOJqE2QHU5P5_Bj1YzmJMlmfapy35UoyixjThmzwMsbvml8gIGGRiENwEgAPciUq1IOEp",
                    data={
                        'title': "Новости/Жаңылыктар",
                        'body': self.name
                    })


class Notification(models.Model):
    news = models.ForeignKey('News', related_name='not1',
                             on_delete=models.CASCADE, null=True, blank=True)

    game = models.ForeignKey('GameQuizGame', related_name='not1',
                             on_delete=models.CASCADE, null=True, blank=True)

    user = models.ForeignKey('Users', related_name='not1',
                             on_delete=models.CASCADE, null=True, blank=True)
    is_view = models.BooleanField(default=False, null=True, blank=True)
    title = models.CharField(max_length=300, null=True, blank=True)
    body = models.CharField(max_length=5000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, blank=True, null=True)


class Game(models.Model):
    class Meta:
        verbose_name = 'Дуэль'
        verbose_name_plural = 'Дуэли'

    lang = models.IntegerField(choices=LANG_CHOICES, null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name='Предмет')
    image = models.ImageField(upload_to=image_upload_to, null=True, blank=True, verbose_name='картинки')

    def __str__(self):
        return self.name


class GameQuiz(models.Model):
    class Meta:
        verbose_name = 'Тест для Дуэли'
        verbose_name_plural = 'Тесты для Дуэли'

    test = models.ForeignKey('Game', verbose_name='Тест', related_name='game',
                             on_delete=models.CASCADE)
    question = models.TextField(null=True, blank=True, verbose_name='вопрос')
    answer_a = models.TextField(null=True, blank=True, verbose_name='ответ_а')
    answer_b = models.TextField(null=True, blank=True, verbose_name='ответ_б')
    answer_c = models.TextField(null=True, blank=True, verbose_name='ответ_в')
    answer_d = models.TextField(null=True, blank=True, verbose_name='ответ_г')
    answer_e = models.TextField(null=True, blank=True, verbose_name='ответ_д')
    true_answer = models.CharField(max_length=1, verbose_name="правильный ответ")
    duration = models.IntegerField(null=True, blank=True, verbose_name='время одного вопроса')

    def __str__(self):
        return self.question


class DayQuiz(models.Model):
    class Meta:
        verbose_name = 'Каждодневный вопрос'
        verbose_name_plural = 'Каждодневные вопросы'

    lang = models.IntegerField(choices=LANG_CHOICES, null=True, blank=True)
    question = models.TextField(null=True, blank=True, verbose_name='вопрос')
    answer_a = models.TextField(null=True, blank=True, verbose_name='ответ_а')
    answer_b = models.TextField(null=True, blank=True, verbose_name='ответ_б')
    answer_c = models.TextField(null=True, blank=True, verbose_name='ответ_в')
    answer_d = models.TextField(null=True, blank=True, verbose_name='ответ_г')
    answer_e = models.TextField(null=True, blank=True, verbose_name='ответ_д')
    true_answer = models.TextField(max_length=1, verbose_name="правильный ответ")
    date = models.DateField(verbose_name='дата')
    duration = models.IntegerField(null=True, blank=True, verbose_name='время одного вопроса')

    def __str__(self):
        return self.question


class GameQuizGame(models.Model):

    quiz = models.CharField(max_length=500)
    category = models.CharField(max_length=500,null=True,blank=True)

    user_owner = models.ForeignKey('Users', verbose_name='Тот Кто отправил', related_name='user_owner',
                                   on_delete=models.CASCADE)

    user_outer = models.ForeignKey('Users', verbose_name='Тот Кто принял', related_name='user_outer',
                                   on_delete=models.CASCADE)

    owner_point = models.IntegerField(verbose_name='рейтинг создателя')
    outer_point = models.IntegerField(verbose_name='рейтинг')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        global user, body
        super().save()
        if self.outer_point == -1:
            user = self.user_outer
            user1 = self.user_owner
            body = "Вам бросил(а) вызов: " + self.user_owner.name+"\nСизге чакырык таштады: "+self.user_owner.name

        elif self.outer_point > -1:
            user = self.user_owner
            user1 = self.user_outer
            if self.outer_point > self.owner_point:
                body = "Вы проиграли: " + self.user_outer.name+"\n Сиз жеңилдиңиз: " + self.user_outer.name
            elif self.outer_point < self.owner_point:
                body = "Вы выиграли: " + self.user_outer.name+"\n Сиз жеңдиңиз: " + self.user_outer.name
            else:
                body = "У вас ничья с: " + self.user_outer.name+"\n Тең чыгуу: " + self.user_outer.name

        Notification(game=self, user=user, title="Дуэль", body=body).save()
        if user.is_notification is None or user.is_notification is True:
            Device.objects.filter(users=user).send_message(
                api_key="AAAA0w0fEAM:APA91bHCgAJUjQnWUMjBQFUrX8tbnhwTkNzw8RoLEMMMxZhTmDmayy2TQnPz3v26t7Y051wXOJqE2QHU5P5_Bj1YzmJMlmfapy35UoyixjThmzwMsbvml8gIGGRiENwEgAPciUq1IOEp",
                data={
                    'title': "Дуэль",
                    'body': body
                })


class QuizCount(models.Model):
    date = models.DateField()
    true_quiz = models.IntegerField()
    false_quiz = models.IntegerField()


class Device(FCMDevice):
    users = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name='device'
    )


class Quote(models.Model):
    quote = models.TextField(max_length=1000,null=True,blank=True)


class MyNotif(models.Model):
    class Meta:
        verbose_name = 'Уведомление'
        verbose_name_plural = 'Уведомления'

    name = models.CharField(max_length=1000, verbose_name='Название')
    desc = models.TextField(verbose_name='Информация')
    created_at = models.DateTimeField(null=True, blank=True, auto_now=True)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()
        users = Users.objects.all()

        Device.objects.all().send_message(
            api_key="AAAA0w0fEAM:APA91bHCgAJUjQnWUMjBQFUrX8tbnhwTkNzw8RoLEMMMxZhTmDmayy2TQnPz3v26t7Y051wXOJqE2QHU5P5_Bj1YzmJMlmfapy35UoyixjThmzwMsbvml8gIGGRiENwEgAPciUq1IOEp",
            data={
                'title': self.name,
                'body': self.desc
            })

