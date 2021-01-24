from rest_framework import serializers
from .models import AwardMerch

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = AwardMerch
        fields = ('id','name', 'design', 'usability','content')