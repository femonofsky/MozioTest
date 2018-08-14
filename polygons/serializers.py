from rest_framework import serializers

from polygons.models import Provider


class ProviderSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    email = serializers.EmailField()
    phone_number = serializers.IntegerField()
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

