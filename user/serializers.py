from rest_framework import serializers

from user.models import User, Location


class UserLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(read_only=True, many=True, slug_field="name")

    class Meta:
        model = User
        fields = "__all__"


class UserCreateSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(required=False, queryset=Location.objects.all(), many=True,
                                            slug_field="name")

    def is_valid(self, *, raise_exception=False):
        self._locations = self.initial_data.pop("location")
        return super().is_valid(rise_exception=raise_exception)

    def create(self, validated_data):
        user = User.object.create(**validated_data)

        for loc in self._locations:
            location, _ = Location.objects.get_on_create(name=loc)
            user.location.add(location)

        return user

    class Meta:
        model = User
        fields = "__all__"


class UserUpdateSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(required=False, queryset=Location.objects.all(), many=True,
                                            slug_field="name")

    def is_valid(self, *, raise_exception=False):
        self._locations = self.initial_data.pop("location")
        return super().is_valid(rise_exception=raise_exception)

    def save(self, **kwargs):
        user = super().save(**kwargs)

        for loc in self._locations:
            location, _ = Location.objects.get_on_create(name=loc)
            user.location.add(location)

        return user

    class Meta:
        model = User
        fields = "__all__"


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "id"
