from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from dj_rest_auth.serializers import TokenSerializer



class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, #response olarak dönmeyecekk bu yüzden write_only=True
        validators = [validate_password],
        #validate password la parolanın tüm şartları taşıyıp 
        #password geçerliyse none, yoksa ValidationError     
        style = {'input_type': 'password'}
    )

    password2 = serializers.CharField(
        write_only=True,
        required = True,
        validators = [validate_password],
        style = {'input_type': 'password'} #password **** şeklinde gelmesi için

    )
    class Meta :
        model = User
        fields = ('username','first_name', 'last_name',
         'email', 'password', 'password2')

    def create(self, validated_data):
        password = validated_data.get('password')
        validated_data.pop('password2')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
        
        #create methodu ile aldığımız validate datayı user creaation içine koyuyoruz
        #ancak password hariç password u setpassword ile aksi takdirde hata verir,
        #django bunu dbase kaydederken hashliyor dolasıyla düz metin gibi gönderemiyoruz. 


    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return data

class UserTokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email")

# Login yaptığımız zaman token ile diğer user bilgilerini de göndermek istiyoruz.


class CustomTokenSerializer(TokenSerializer):

    user = UserTokenSerializer(read_only=True)

    class Meta(TokenSerializer.Meta):
        fields = ("key", "user")
        # key --> token
        # user'ın bilgilerini göndermek için user field'ını ekliyoruz.
       
    