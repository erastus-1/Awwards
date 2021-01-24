from rest_framework import serializers
from .models import AwardMerch

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = AwardMerch
        fields = ('name', 'design', 'usability','content')