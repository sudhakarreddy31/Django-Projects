from rest_framework import serializers
from ecommerceapi.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"
        depth=1     # Accessing Foregn Key Relation In Frontend
        # fields = ['product_id','name']


# using sample serializers

class SampleSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()