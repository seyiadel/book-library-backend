from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password = None):
        if not email:
            raise ValueError("This is not an email, Please check")
        user = self.model(
            first_name= first_name,
            last_name = last_name,
            email= self.normalize_email(email)
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        if not email:
            raise ValueError("This is not an email, Please check")
        user = self.model(
            email= self.normalize_email(email)
        )
        user.is_active = True
        user.is_admin = True
        # Deals with the Password Hashing
        user.set_password(password)
        user.save()
        return user

    def create_staffuser(self, first_name, last_name, email, password=None):
        if not email:
            raise ValueError("Enter a valid email address")
        user= self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
        )
        user.is_active = True
        user.is_staff=True
        user.set_password(password)
        user.save()
        return user