from django.db import models

# Create your models here.

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=50, verbose_name='Отчество')
    phone = models.IntegerField(verbose_name='Телефон')


    def __str__(self):
        return self.name+' '+self.patronymic+' '+self.surname
    def __unicode__(self):
        return self.name+' '+self.patronymic+' '+self.surname

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural ='Клиенты'


'''CREATE TABLE IF NOT EXISTS Branch
        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name VARCHAR(30) NOT NULL,
        city VARCHAR(30) NOT NULL,
        adress VARCHAR(30) NOT NULL,
        phone VARCHAR(12) NOT NULL);'''

class Branch(models.Model):
    id= models.AutoField(primary_key =True)
    name= models.CharField(max_length=120, verbose_name='Название')
    city = models.CharField(max_length=120, verbose_name='Город')
    adress= models.CharField(max_length=120, verbose_name='Адрес')
    phone = models.IntegerField(verbose_name='Телефон')


    def __str__(self):
       return self.name
    def __unicode__(self):
       return self.name


    class Meta:
        verbose_name = 'Отделы'
        verbose_name_plural ='Отделы'


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30,verbose_name='Имя')
    surname = models.CharField(max_length=50,verbose_name='Фамилия')
    patronymic = models.CharField(max_length=50,verbose_name='Отчество')
    phone = models.IntegerField(verbose_name='Телефон')
    email = models.EmailField(max_length=254, null=True, blank=True, verbose_name='Почта')
    branch=models.ForeignKey(Branch, on_delete=models.CASCADE)


    def __str__(self):
        return self.name+' '+self.patronymic+' '+self.surname
    def __unicode__(self):
        return self.name+' '+self.patronymic+' '+self.surname

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural ='Сотрудники'


'''CREATE TABLE IF NOT EXISTS Contract
        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
        date TIMESTAMP NOT NULL,
        insurance_summ REAL NOT NULL,
        insurance_payment REAL NOT NULL,
        branch_id INTEGER,
        employee_id INTEGER,
        client_id INTEGER,
        object VARCHAR(30) NOT NULL,
        name_of_insurance VARCHAR(30) NOT NULL, );'''

class Contract(models.Model):
    id= models.AutoField(primary_key =True)
    name_of_insurance = models.CharField(max_length=120, verbose_name='Тип страхования')
    object = models.CharField(max_length=120, verbose_name='Объект страхования')
    date=models.DateTimeField(verbose_name='Дата заключения')
    insurance_summ=models.FloatField(verbose_name='Сумма страхования')
    insurance_payment=models.FloatField(verbose_name='Стоимость страхования')
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __unicode__(self):
       return self.date

    def __str_(self):
       return self.date

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural ='Договоры'
