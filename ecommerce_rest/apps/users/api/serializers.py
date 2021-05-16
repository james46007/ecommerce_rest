from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

    def to_representation(self,instance):
        return {
            'id': instance['id'],
            'username': instance['username'],
            'email': instance['email'],
            'password': instance['password']
        }

# class TestUserSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length = 20)
#     email = serializers.EmailField()

#     def validate_name(self,value):
#         #validacion personalizada
#         if 'test2' in value:
#             raise serializers.ValidationError('Error, no puede existir un usuraio con ese nombre.')
#         return value
    
#     def validate_email(self,value):
#         #validacion personalizada
#         if value == '':
#             raise serializers.ValidationError('Tiene que indicar un correo.')

#         if self.validate_name(self.context['name']) in value:
#             raise serializers.ValidationError('El email no puede contener el nombre.')    

#         return value

#     def validate(self,data):
#         #validacion personalizada
#         # if data['name'] in data['email']:
#         #     raise serializers.ValidationError('El email no puede contener el nombre.')        
#         return data

#     def create(self,validated_data):
#         return self.objects.create(**validated_data)
#         # print(validated_data)

#     def update(self,instance,validated_data):
#         print(instance)