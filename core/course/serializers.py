from rest_framework import serializers 


from .models import Course, LessonCourse


class CourseSerializer(serializers.ModelSerializer):
	lesson_course = serializers.PrimaryKeyRelatedField(many=True, queryset=LessonCourse.objects.all())

	class Meta:
		model = Course 
		fields = ('url', 
					'id', 
					'name',
					'slug',
					'image',
					'little_description',
					'description',
					'price',
					'week_one',
					'description_week_one',
					'week_second',
					'description_week_second',
					'week_third',
					'description_week_third',
					'week_fourth',
					'description_week_fourth',
					'lesson_course',
					)

class LessonCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = LessonCourse
        fields = ('nameCourse',
					'nameDay',
					'day',
					'slug',
					'description',
					'url_video',)
    