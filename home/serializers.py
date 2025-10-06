from rest_framework import serializers
from .models import UserDetails,Color

class LoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField()

class ColorSerializer(serializers.ModelSerializer):
      class Meta:
        model= Color
        fields=["color_name"]

class PeopleSerializer(serializers.ModelSerializer):
    color=ColorSerializer()
    color_info=serializers.SerializerMethodField()

    class Meta:
        model= UserDetails
        fields="__all__"
        # depth=1 (index value data will be shown)
        # fields=["name"]


    def get_color_info(self,obj):
        color_obj=Color.objects.get(id=obj.color.id)
        return {'color_name':color_obj.color_name,'hex_code':'#000'}  #customer values

    def validate(self,data):
        special_characters="!@#$%^&*()-+?/,<>"
        if any(c in special_characters for c in data['name']):
            raise serializers.ValidationError("name cannot contain special characters")
        if data['age']<18:
            raise serializers.ValidationError('age should be greater than 18') 
        return data




 