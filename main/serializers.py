from rest_framework import serializers
from . import models


from rest_framework import serializers
from . import models

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = ['id', 'user', 'address']
        
    # إذا كنت تصر على جلب بيانات المستخدم كاملة عند القراءة (GET) فقط دون تعطيل الإنشاء (POST):
    def to_representation(self, instance):
        response = super().to_representation(instance)
        # سيقوم بجلب تفاصيل المستخدم بدلاً من الـ ID فقط عند عرض البيانات
        response['user'] = {
            "id": instance.user.id,
            "username": instance.user.username,
            "email": instance.user.email
        }
        return response
