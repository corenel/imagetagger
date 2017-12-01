from rest_framework.serializers import ModelSerializer

from .models import Annotation, AnnotationType, AnnotationFormat


class AnnotationFormatSerializer(ModelSerializer):

    class Meta:
        model = AnnotationFormat
        fields = (
            'id',
            'name',
            'field',
        )


class AnnotationTypeSerializer(ModelSerializer):
    class Meta:
        model = AnnotationType
        fields = (
            'id',
            'name',
            'format',
        )

    annotation_format = AnnotationFormatSerializer(read_only=True)


class AnnotationSerializer(ModelSerializer):
    class Meta:
        model = Annotation
        fields = (
            'annotation_type',
            'content',
            'id',
            'vector',
        )

    annotation_type = AnnotationTypeSerializer(read_only=True)
