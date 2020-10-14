from rest_framework import serializers
from ..models import Answer, Question
import locale

locale.setlocale(locale.LC_ALL, 'it_IT.UTF-8')

class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    likes_count = serializers.SerializerMethodField(read_only=True)
    user_has_voted = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Answer
        exclude = ["question", "voter", "updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime('%d %B %Y')

    def get_likes_count(self, instance):
        return instance.voters.count()

    def get_user_has_voted(self, instance):
        request = self.context.get("request")
        return instance.voters.filter(pk=request.user.pk).exist()


class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    answers_count = serializers.SerializerMethodField(read_only=True)
    user_has_answered = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Question
        exclude = ["update_at"]

    def get_answers_count(self, instance):
        return instance.answers.count()

    def get_created_at(self, instance):
        return instance.created_at.strftime('%d %B %Y')

    def get_likes_count(self, instance):
        return instance.voters.count()

    def get_user_has_answered(self, instance):
        request = self.context.get("request")
        return instance.answers.filter(author=request.user).exists()

