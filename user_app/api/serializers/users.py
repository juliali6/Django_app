# from rest_framework import serializers
# from ...models import User
#
#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User  # импортируем обязательно из нашего модуля
#         fields = ('id', 'username', 'email', 'first_name', 'last_name')
#         read_only_fields = ('id', 'username', 'email')
#
#     username = serializers.CharField(min_length=3, required=True)
#     password = serializers.CharField(min_length=8, required=True,
#                                      write_only=True)  # write_only - скрывает введенные данные при регистрации в API
#     email = serializers.EmailField(required=True, write_only=True)