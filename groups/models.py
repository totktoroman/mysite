from django.db import models

# Create your models here.
group_choices = (
            ('МОАИС', 'Мат. обеспечение и администрирование информационных систем'),
            ('ПИ', 'Прикладная информатика'),
            ('ПМ', 'Прикладная математика и инофрматика'),
            ('Пед. обр', 'Педагогическое образование с двумя профилями подготовки'),
            ('Не студенческая группа', 'Не студенческиая группа'),
        )
class Group(models.Model):
    group_number = models.CharField('Номер группы', max_length=10, unique=True)
    group_title = models.CharField('Направление', max_length=250, choices=group_choices)

    def __str__(self):
        return self.group_title

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

class Student(models.Model):
    student_surname = models.CharField('Фамилия', max_length=50)
    student_name = models.CharField('Имя', max_length=50)
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    account_id = models.IntegerField('id аккаунта')

    def __str__(self):
        return self.student_surname +' '+ self.student_name

    def info(self):
        return 'Фамилия: ' +self.student_surname +'Имя: '+ self.student_name + ' Аккаунт: '+ str(self.account_id)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'