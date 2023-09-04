from django.db import models


class Address(models.Model):
    country = models.CharField(max_length=50, verbose_name='Country')
    state = models.CharField(max_length=50, verbose_name='State')
    city = models.CharField(max_length=50, verbose_name='City')
    street = models.CharField(max_length=100, verbose_name='Street')
    postal_code = models.CharField(max_length=10, verbose_name='Postal Code')

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'


class Person(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='First Name')
    middle_name = models.CharField(max_length=50, verbose_name='Middle Name')
    last_name = models.CharField(max_length=50, verbose_name='Last Name')
    phone_number = models.CharField(max_length=15, verbose_name='Phone Number')
    e_mail = models.EmailField(max_length=100, verbose_name='Email')
    address = models.ForeignKey(Address, on_delete=models.CASCADE, verbose_name='Address')

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'


class Student(models.Model):
    group_number = models.CharField(max_length=10, verbose_name='Group Number')
    average_mark = models.FloatField(verbose_name='Average Mark')
    scholarship = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Scholarship')
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='Person')

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'


class Teacher(models.Model):
    grade = models.CharField(max_length=10, verbose_name='Grade')
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Salary')
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='Person')

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
