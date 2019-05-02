from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.reverse import reverse 
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Course , LessonCourse
from .serializers import CourseSerializer, LessonCourseSerializer
# Create your views here.

@api_view(['GET'])
def api_root(request, format=None):
	return Response({
		'courses': reverse('course-list', request=request, format=format),
		'lessons': reverse('lesson-list', request=request, format=format),

		})


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
	"""
	This viewset automatically provides 'list' and 'detail' actions.
	"""
	queryset = Course.objects.all()
	serializer_class = CourseSerializer


class LessonCourseViewSet(viewsets.ReadOnlyModelViewSet):
	"""
	This viewset automatically provides 'list' and 'detail' actions.
	"""
	queryset = LessonCourse.objects.all()
	serializer_class = LessonCourseSerializer