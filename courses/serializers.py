from rest_framework import serializers

from courses.models import Course, Section


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        exclude = ("course",)


class CourseSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True)

    class Meta:
        model = Course
        fields = "__all__"

    def create(self, validated_data):
        sections_data = validated_data.pop("sections")
        course = Course.objects.create(**validated_data)
        sections = []
        for section_data in sections_data:
            sections.append(Section(course=course, **section_data))
        Section.objects.bulk_create(sections)
        return course

    def update(self, instance, validated_data):
        # TODO: update sections
        return super().update(instance, validated_data)
