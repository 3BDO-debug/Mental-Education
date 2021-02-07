from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
#from Educational_Stages.models import Subject
from Courses.models import Course
# Create your models here.


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, user_email, user_full_name, password=None):
        if not user_email:
            raise ValueError("User Must Have an Email")
        user = self.model(
            user_email=self.normalize_email(user_email), user_full_name=user_full_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_email, user_full_name, password=None):
        if not user_email:
            raise ValueError("User Must Have an Email")
        user = self.model(
            user_email=self.normalize_email(user_email), user_full_name=user_full_name
        )
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True

        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    user_full_name = models.CharField(max_length=750, verbose_name="User's Full Name")
    user_profile_pic = models.ImageField(
        default="/styling/assets/images/avatar.png",
        upload_to="Users_Profile_Pics",
    )
    user_email = models.EmailField(unique=True, verbose_name="User's Email Address")
    user_selected_courses = models.ManyToManyField(Course, verbose_name="User's on going courses", blank=True)
    
    joined_at = models.DateTimeField(auto_now_add=True, verbose_name="Joined at")
    last_login = models.DateTimeField(
        verbose_name="last login",
        auto_now_add=True,
    )
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False, verbose_name="Account Activated")
    is_teacher = models.BooleanField(default=False, verbose_name="Teacher Account")
    objects = UserManager()
    USERNAME_FIELD = "user_email"
    REQUIRED_FIELDS = ["user_full_name"]

    def __str__(self):
        return self.user_full_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True