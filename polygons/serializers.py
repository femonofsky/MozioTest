from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework.validators import UniqueValidator


from polygons.models import Provider, ServiceArea


class ProviderSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    email = serializers.EmailField(validators=[UniqueValidator(queryset=Provider.objects.all())])
    phone_number = serializers.CharField()
    language = serializers.CharField()
    currency = serializers.CharField()

    def create(self, validated_data):
        provider = Provider(**validated_data)
        provider.save()
        return provider

    def update(self, instance, validated_data):
        instance.name = validated_data["name"]
        instance.email = validated_data["email"]
        instance.phone_number = validated_data["phone_number"]
        instance.language = validated_data["language"]
        instance.currency = validated_data["currency"]
        instance.save()
        return instance

    class Meta:
        model = Provider
        fields = '__all__'


class ServiceAreaSerializer(GeoFeatureModelSerializer):
    provider = ProviderSerializer(read_only=True)
    provider_id = serializers.PrimaryKeyRelatedField(source="provider", queryset=Provider.objects.all())

    class Meta:
        model = ServiceArea
        geo_field = 'polygon'
        fields = '__all__'

