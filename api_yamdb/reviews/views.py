from django.shortcuts import get_object_or_404
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from .models import Review, Title

from .permissions import IsAuthorModeratorAdminSuperuser
from .serializers import CommentsSerializer, ReviewsSerializer


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,
                          IsAuthorModeratorAdminSuperuser,)

    def get_title(self):
        return get_object_or_404(Title, pk=self.kwargs.get('title_id'))

    def get_queryset(self):
        title = self.get_title()
        return title.reviews.all()

    def perform_create(self, serializer):
        title = self.get_title()
        serializer.save(
            author=self.request.user,
            title=title,
        )


class CommentViewSet(ModelViewSet):
    serializer_class = CommentsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,
                          IsAuthorModeratorAdminSuperuser,)

    def get_review_and_title(self):
        title_id = self.kwargs.get('title_id')
        review_id = self.kwargs.get('review_id')
        return get_object_or_404(
            Review.objects.filter(title_id=title_id), pk=review_id
        )

    def get_queryset(self):
        review = self.get_review_and_title()
        return review.comments.all()

    def perform_create(self, serializer):
        review = self.get_review_and_title()
        serializer.save(
            author=self.request.user,
            review=review
        )
