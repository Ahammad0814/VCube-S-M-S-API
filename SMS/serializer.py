from rest_framework.serializers import ModelSerializer
from .models import LoginData,BatchData,StudentData,DateData,SendOTP

class LoginDataSerializer(ModelSerializer):
    class Meta:
        model = LoginData
        fields = '__all__'
        
class BatchDataSerializer(ModelSerializer):
    class Meta:
        model = BatchData
        fields = '__all__'
        
class StudentDataSerializer(ModelSerializer):
    class Meta:
        model = StudentData
        fields = '__all__'
        
class DateDataSerializer(ModelSerializer):
    class Meta:
        model = DateData
        fields = '__all__'
        
class SendOTPSerializer(ModelSerializer):
    class Meta:
        model = SendOTP
        fields = '__all__'