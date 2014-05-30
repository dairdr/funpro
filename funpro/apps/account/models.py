# -*- encoding: utf-8 -*-
"""Defines all Login's models.

Many of these modules are admin by Django Admin UI.

"""
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

class UserManager(BaseUserManager):
	"""User Manager"""
	def _create_user(self, email, first_name, password, is_staff, is_superuser, **extra_fields):
		"""Creates and saves a User with the given username, email and password."""
		now = timezone.now()
		if not email:
			raise ValueError('The given email must be set')
		email = self.normalize_email(email)
		user = self.model(email=email, first_name=first_name, is_staff=is_staff, is_active=True, is_superuser=is_superuser, last_login=now, date_joined=now, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, email, first_name, password, **extra_fields):
		return self._create_user(email, first_name, password, False, False, **extra_fields)

	def create_superuser(self, email, first_name, password, **extra_fields):
		return self._create_user(email, first_name, password, True, True, **extra_fields)

class Student(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(db_column='email', blank=False, unique=True)
	first_name = models.CharField(db_column='first_name', max_length=45, blank=False, null=False)
	last_name = models.CharField(db_column='last_name', max_length=45, blank=True, null=True)
	date_of_birth = models.DateField(db_column='date_of_birth', null=True)
	is_staff = models.BooleanField(db_column='is_staff', default=False)
	is_active = models.BooleanField(db_column='is_active', default=True)
	date_joined = models.DateTimeField(db_column='date_joined', default=timezone.now)

	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name']

	class Meta:
		db_table = 'account_student'
		ordering = ['id']
		verbose_name = 'student'
		verbose_name_plural = 'students'

	def get_full_name(self):
		"""Returns the first_name plus the last_name, with a space in between."""
		full_name = '%s %s' % (self.first_name, self.last_name)
		return full_name.strip()

	def get_short_name(self):
		"Returns the short name for the user."
		return self.first_name

	def email_user(self, subject, message, from_email=None, **kwargs):
		"""Sends an email to this User."""
		send_mail(subject, message, from_email, [self.email], **kwargs)