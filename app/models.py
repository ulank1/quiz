from django.db import models

# Create your models here.
from django.db.models import Q
from fcm_django.models import FCMDevice


def image_upload_to(instance, filename):
    return "images/%s" % (filename)


LANG_CHOICES = ((1, 'KG'), (2, 'RU'))
ORT_DESC_CHOICES = (
(0, 'Математика 1'), (1, 'Математика 2'), (2, 'Аналогия'), (3, 'Чтение и понимание'), (4, 'Грамматика'), (5, 'Общее'))
ORT_TEST_CHOICES = (
(0, 'Математика 1'), (1, 'Математика 2'), (2, 'Аналогия'), (3, 'Чтение и понимание'), (4, 'Грамматика'))
LIKE_CHOICES = ((0, "No"), (1, 'Like'), (2, 'UnLike'))


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
    win = models.IntegerField(null=True, blank=True, default=0)
    lose = models.IntegerField(null=True, blank=True, default=0)
    draw = models.IntegerField(null=True, blank=True, default=0)
    is_admin = models.BooleanField(default=False, null=True, blank=True)

    # rating = models.IntegerField(max_length=100, null=True, blank=True, verbose_name='рейтинг')


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
        Device.objects.all().send_message(
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

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()
        notif = Notification.objects.order_by('-id').filter(user=self.user)
        if len(notif) > 30:
            for i in range(30, len(notif)):
                notif[i].delete()


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
    date = models.DateField(verbose_name='дата')

    def __str__(self):
        return self.question


class GameQuizGame(models.Model):
    quiz = models.CharField(max_length=500)
    category = models.CharField(max_length=500, null=True, blank=True)

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
            body = "Вам бросил(а) вызов: " + self.user_owner.name + "\nСизге чакырык таштады: " + self.user_owner.name

        elif self.outer_point > -1:
            user = self.user_owner
            user1 = self.user_outer
            if self.outer_point > self.owner_point:
                user.lose = user.lose + 1
                user1.win = user1.win + 1
                body = "Вы проиграли: " + self.user_outer.name + "\n Сиз жеңилдиңиз: " + self.user_outer.name
            elif self.outer_point < self.owner_point:
                user.win = user.win + 1
                user1.lose = user1.lose + 1
                body = "Вы выиграли: " + self.user_outer.name + "\n Сиз жеңдиңиз: " + self.user_outer.name
            else:
                user.draw = user.draw + 1
                user1.draw = user1.draw + 1
                body = "У вас ничья с: " + self.user_outer.name + "\n Тең чыгуу: " + self.user_outer.name

            user.save()
            user1.save()

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
    lang = models.IntegerField(choices=LANG_CHOICES, null=True, blank=True)
    quote = models.TextField(max_length=1000, null=True, blank=True)


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


class CommentQuestion(models.Model):
    class Meta:
        verbose_name = "Коментарий к задаче дня"
        verbose_name_plural = "Коментарии к задаче дня"

    quiz = models.ForeignKey(
        DayQuiz,
        on_delete=models.CASCADE,
        related_name='Comment'
    )
    created_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='Comment', null=True, blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    message = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.message


class AnswerToComment(models.Model):
    class Meta:
        verbose_name = "Ответ к коментарию к задаче дня"
        verbose_name_plural = "Ответы к коментарию к задаче дня"

    created_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='answer', null=True, blank=True)
    comment = models.ForeignKey(CommentQuestion, on_delete=models.CASCADE, related_name='answer')
    name = models.CharField(max_length=100, blank=True, null=True)
    message = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.message


class LikeQuiz(models.Model):
    like = models.IntegerField(choices=LIKE_CHOICES, null=True, blank=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='like_quiz', null=True, blank=True)
    comment = models.ForeignKey(CommentQuestion, on_delete=models.CASCADE, related_name='like_quiz', null=True,
                                blank=True)


class LikeAnswerQuiz(models.Model):
    like = models.IntegerField(choices=LIKE_CHOICES, null=True, blank=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='like_answer_quiz', null=True, blank=True)
    answer = models.ForeignKey(AnswerToComment, on_delete=models.CASCADE, related_name='like_answer_quiz', null=True,
                               blank=True)


class Friend(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='friend_owner', null=True, blank=True)
    friend = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='friend', null=True, blank=True)
    is_active = models.BooleanField(null=True, blank=True, default=True)


class Forum(models.Model):
    class Meta:
        verbose_name_plural = "Название форума"
        verbose_name = "Название форума"

    lang = models.IntegerField(choices=LANG_CHOICES, null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    image = models.ImageField(upload_to=image_upload_to, null=True, blank=True, verbose_name='картинка')
    title = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(null=True, blank=True, default=True)


class Topic(models.Model):
    class Meta:
        verbose_name_plural = "Тема форума"
        verbose_name = "Тема форума"

    created_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='topic', null=True, blank=True)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name='topic', null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=image_upload_to, null=True, blank=True, verbose_name='картинка')
    is_active = models.BooleanField(null=True, blank=True, default=True)
    comment_count = models.IntegerField(null=True, blank=True, default=0)


class Topic1(models.Model):
    class Meta:
        verbose_name_plural = "Тема форума"
        verbose_name = "Тема форума"

    created_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='topic1', null=True, blank=True)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name='topic1', null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=image_upload_to, null=True, blank=True, verbose_name='картинка')
    is_active = models.BooleanField(null=True, blank=True, default=True)
    comment_count = models.IntegerField(null=True, blank=True, default=0)


class CommentForum(models.Model):
    class Meta:
        verbose_name = "Коментарий к Форуму"
        verbose_name_plural = "Коментарии к Форуму"

    topic = models.ForeignKey(
        Topic1,
        on_delete=models.CASCADE,
        related_name='comment'
    )
    created_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='comment_forum', null=True, blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    message = models.CharField(max_length=500, blank=True, null=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()
        self.topic.comment_count = self.topic.comment_count + 1
        self.topic.save()


class AnswerToCommentForum(models.Model):
    class Meta:
        verbose_name = "Ответ к коментарию к Форуму"
        verbose_name_plural = "Ответы к коментарию к Форуму"

    created_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='answer_forum', null=True, blank=True)
    comment = models.ForeignKey(CommentForum, on_delete=models.CASCADE, related_name='answer')
    name = models.CharField(max_length=100, blank=True, null=True)
    message = models.CharField(max_length=500, blank=True, null=True)


class LikeForum(models.Model):
    created_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    like = models.IntegerField(choices=LIKE_CHOICES, null=True, blank=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='like_forum', null=True, blank=True)
    comment = models.ForeignKey(CommentForum, on_delete=models.CASCADE, related_name='like_forum', null=True,
                                blank=True)


class LikeAnswerForum(models.Model):
    created_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    like = models.IntegerField(choices=LIKE_CHOICES, null=True, blank=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='like_answer_forum', null=True, blank=True)
    answer = models.ForeignKey(AnswerToCommentForum, on_delete=models.CASCADE, related_name='like_answer_forum',
                               null=True,
                               blank=True)


class PayOrt(models.Model):
    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'

    created_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='pay', null=True, blank=True)
    is_used = models.BooleanField(default=False, null=True, blank=True, verbose_name="использовано?")
    used_time = models.DateTimeField(null=True, blank=True)


class CategoryOrt(models.Model):
    class Meta:
        verbose_name = 'Название пробного теста'
        verbose_name_plural = 'Названии пробного теста'

    title = models.CharField(max_length=255, null=True, blank=True)
    lang = models.IntegerField(choices=LANG_CHOICES, null=True, blank=True)


class Math1Ort(models.Model):
    class Meta:
        verbose_name = 'Пробный тест'
        verbose_name_plural = 'Пробные тесты'

    category = models.ForeignKey('CategoryOrt', verbose_name='название пробного теста', related_name='math1',
                                 on_delete=models.CASCADE)
    type_of_test = models.IntegerField(choices=ORT_TEST_CHOICES,null=True,blank=True)
    question = models.TextField(null=True, blank=True, verbose_name='вопрос')
    answer_a = models.TextField(null=True, blank=True, verbose_name='ответ_а')
    answer_b = models.TextField(null=True, blank=True, verbose_name='ответ_б')
    answer_c = models.TextField(null=True, blank=True, verbose_name='ответ_в')
    answer_d = models.TextField(null=True, blank=True, verbose_name='ответ_г')
    answer_e = models.TextField(null=True, blank=True, verbose_name='ответ_д')
    true_answer = models.CharField(max_length=1, verbose_name="правильный ответ")


class Math2Ort(models.Model):
    class Meta:
        verbose_name = 'Пробный тест (Математика2)'
        verbose_name_plural = 'Пробные тесты (Математика2)'

    category = models.ForeignKey('CategoryOrt', verbose_name='название пробного теста', related_name='math2',
                                 on_delete=models.CASCADE)
    question = models.TextField(null=True, blank=True, verbose_name='вопрос')
    answer_a = models.TextField(null=True, blank=True, verbose_name='ответ_а')
    answer_b = models.TextField(null=True, blank=True, verbose_name='ответ_б')
    answer_c = models.TextField(null=True, blank=True, verbose_name='ответ_в')
    answer_d = models.TextField(null=True, blank=True, verbose_name='ответ_г')
    answer_e = models.TextField(null=True, blank=True, verbose_name='ответ_д')
    true_answer = models.CharField(max_length=1, verbose_name="правильный ответ")


class AnalogOrt(models.Model):
    class Meta:
        verbose_name = 'Пробный тест (Аналогии)'
        verbose_name_plural = 'Пробные тесты (Аналогии)'

    category = models.ForeignKey('CategoryOrt', verbose_name='название пробного теста', related_name='analog',
                                 on_delete=models.CASCADE)
    question = models.TextField(null=True, blank=True, verbose_name='вопрос')
    answer_a = models.TextField(null=True, blank=True, verbose_name='ответ_а')
    answer_b = models.TextField(null=True, blank=True, verbose_name='ответ_б')
    answer_c = models.TextField(null=True, blank=True, verbose_name='ответ_в')
    answer_d = models.TextField(null=True, blank=True, verbose_name='ответ_г')
    answer_e = models.TextField(null=True, blank=True, verbose_name='ответ_д')
    true_answer = models.CharField(max_length=1, verbose_name="правильный ответ")


class UnderstandOrt(models.Model):
    class Meta:
        verbose_name = 'Пробный тест (Чтение и понимание)'
        verbose_name_plural = 'Пробные тесты (Чтение и понимание)'

    category = models.ForeignKey('CategoryOrt', verbose_name='название пробного теста', related_name='understand',
                                 on_delete=models.CASCADE)
    question = models.TextField(null=True, blank=True, verbose_name='вопрос')
    answer_a = models.TextField(null=True, blank=True, verbose_name='ответ_а')
    answer_b = models.TextField(null=True, blank=True, verbose_name='ответ_б')
    answer_c = models.TextField(null=True, blank=True, verbose_name='ответ_в')
    answer_d = models.TextField(null=True, blank=True, verbose_name='ответ_г')
    answer_e = models.TextField(null=True, blank=True, verbose_name='ответ_д')
    true_answer = models.CharField(max_length=1, verbose_name="правильный ответ")


class GrammarOrt(models.Model):
    class Meta:
        verbose_name = 'Пробный тест (Грамматика)'
        verbose_name_plural = 'Пробные тесты (Грамматика)'

    category = models.ForeignKey('CategoryOrt', verbose_name='название пробного теста', related_name='grammar',
                                 on_delete=models.CASCADE)
    question = models.TextField(null=True, blank=True, verbose_name='вопрос')
    answer_a = models.TextField(null=True, blank=True, verbose_name='ответ_а')
    answer_b = models.TextField(null=True, blank=True, verbose_name='ответ_б')
    answer_c = models.TextField(null=True, blank=True, verbose_name='ответ_в')
    answer_d = models.TextField(null=True, blank=True, verbose_name='ответ_г')
    answer_e = models.TextField(null=True, blank=True, verbose_name='ответ_д')
    true_answer = models.CharField(max_length=1, verbose_name="правильный ответ")


class PointsOrt(models.Model):
    class Meta:
        verbose_name = 'Балл пробного теста'
        verbose_name_plural = 'Баллы пробного теста'

    created_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='ort', null=True, blank=True)
    point = models.IntegerField(null=True, blank=True)


class DescOrt(models.Model):
    class Meta:
        verbose_name = 'Информация об Орт'
        verbose_name_plural = 'Информации об Орт'

    lang = models.IntegerField(choices=LANG_CHOICES, null=True, blank=True)
    category = models.IntegerField(choices=ORT_DESC_CHOICES, null=True, blank=True)
    desc = models.TextField(null=True, blank=True, verbose_name="Описание")
    title = models.CharField(max_length=255, null=True, blank=True, verbose_name="Название")
    created_at = models.DateTimeField(null=True, blank=True, auto_now=True)
