from rest_framework.serializers import ModelSerializer, Serializer, CharField, ValidationError, EmailField
from library_App.models import User, Book
from django.contrib.auth import authenticate


class UserSerializer(ModelSerializer):
    password = CharField(max_length=390, write_only=True)
    confirm_password = CharField(max_length=390, write_only=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'confirm_password','created_at']

    def create(self, validated_data):
        if validated_data['confirm_password'] != validated_data['password']:
            raise ValidationError("Password and Confirm Password are not same")
        elif len(validated_data["password"]) <= 8:
            raise ValidationError("Password is not strong enough, Must be within 9 and 15 characters")
        else:
           user = User.objects.create_user(validated_data['first_name'], validated_data['last_name'], validated_data['email'], validated_data['password'])
           return user
    

class  LogInUserSerializer(Serializer):
    email = EmailField()
    password = CharField(max_length=13, write_only=True)
    

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        check_user = User.objects.filter(email=email)

        if email and password:
            if not check_user.exists():
                raise ValidationError("Email do not exist. Sign Up")
            elif check_user.get(email=email).check_password(password) == False:
                    raise ValidationError("Incorrect Password")
            else:
                user = authenticate(request = self.context.get("request"), email=email , password=password)
                
        else:
            message = "Must contain Email and Password respectively"
            raise ValidationError(message)
            
        attrs['user'] = user

        return attrs


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
    
    def create(self, attrs):

        new_book_title = attrs.get('title')
        book_title = Book.objects.filter(title=new_book_title)
        book_extension = attrs.get('upload_book')
    
        if book_title.exists():
            raise ValidationError('Book Exists. Include Edition or Version to make it unique')
        elif ".pdf" not in book_extension.name:
            raise ValidationError('PDF is the accepted format. Check the extension')
        else:
          new_book = Book.objects.create(**attrs)
          return new_book
        