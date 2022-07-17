from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from reviews.models import Comment, Review
from titles.models import Title


class ReviewsSerializer(serializers.ModelSerializer):
    title = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True,
    )
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Review

    def validate(self, data):
        request = self.context['request']
        current_title = get_object_or_404(
            Title, pk=request.parser_context['kwargs'].get('title_id'))

        if request.method == 'POST':
            if current_title.reviews.filter(author=request.user).exists():
                raise serializers.ValidationError(
                    'Вы не можете добавить более одного отзыва на произведение'
                )
        return data


class CommentsSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
