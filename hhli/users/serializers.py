from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from .models import HUser

class HUserRegisterSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(label='ID', read_only=True)
    email = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)

    def validate(self, data):
        """
        Check that password and conifrm password are same.
        """
        password = data.get('password', None)
        confirm_password = data.get('confirm_password', None)
        if not password or not confirm_password or password != confirm_password:
            raise serializers.ValidationError("Password/Confirm password must be same")
        return data

    def validate_email(self, email):
        print 'validate_email is called'
        existing = HUser.objects.filter(email=email).first()
        if existing:
            raise serializers.ValidationError("Email already registered.Forgot password?")
        return email

    class Meta:
        model = HUser
        fields = ('id', 'email','title','first_name','last_name','gender','date_of_birth','height','weight','is_active', 'created_at','updated_at' ,'password',
            'confirm_password',)
        lookup_field = ('id',)

        read_only_fields = ('created_at', 'updated_at', 'is_active')

        def create(self, validated_data):
            print "Create......."
            return HUser.objects.create(**validated_data)

        def update(self, instance, validated_data):

            instance.title 			= validated_data.get('title', instance.title)
            instance.first_name 	= validated_data.get('first_name', instance.first_name)
            instance.last_name 		= validated_data.get('last_name', instance.last_name)
            instance.gender 		= validated_data.get('gender', instance.gender)
            instance.date_of_birth 	= validated_data.get('date_of_birth', instance.date_of_birth)
            instance.height 		= validated_data.get('height', instance.height)
            instance.weight 		= validated_data.get('weight', instance.weight)
            instance.password       = validated_data.get('password', instance.password)

            instance.save()

            if validated_data.get('password', None):
                check_passwords_equal(validated_data)
                instance.set_password(password)
                instance.save()
                update_session_auth_hash(self.context.get('request'), instance)

            return instance


class HUserUpdateSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(label='ID', read_only=True)
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = HUser
        fields = ('id', 'email','title','first_name','last_name','gender','date_of_birth','height','weight','is_active', 'created_at','updated_at' ,'password',
            'confirm_password',)
        lookup_field = ('id',)

        read_only_fields = ('created_at', 'updated_at', 'is_active')


        def update(self, instance, validated_data):

            instance.email          = validated_data.get('email', instance.email)
            instance.title          = validated_data.get('title', instance.title)
            instance.first_name     = validated_data.get('first_name', instance.first_name)
            instance.last_name      = validated_data.get('last_name', instance.last_name)
            instance.gender         = validated_data.get('gender', instance.gender)
            instance.date_of_birth  = validated_data.get('date_of_birth', instance.date_of_birth)
            instance.height         = validated_data.get('height', instance.height)
            instance.weight         = validated_data.get('weight', instance.weight)
            instance.password       = validated_data.get('password', instance.password)

            instance.save()

            if validated_data.get('password', None):
                instance.set_password(password)
                instance.save()
                update_session_auth_hash(self.context.get('request'), instance)

            return instance


