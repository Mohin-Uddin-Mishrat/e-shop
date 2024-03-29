from rest_framework import serializers
from django.contrib.auth.models import User

class registerSerializers(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required = True)
    class Meta :
        model = User
        fields =['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']
    

    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password :
             raise serializers.ValidationError({"error" : "Password does not matchend"})
        if User.objects.filter(email = email).exists() :
             raise serializers.ValidationError({"error" : "With this email a user already exist"})
        
        account = User(username = username , first_name = first_name , last_name = last_name , email = email)

        account.set_password(password)
        account.is_active = False 

        account.save()
        
        return account 
    
class loginSerializer(serializers.Serializer)  :
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
