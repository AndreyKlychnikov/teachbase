from rest_framework import routers

from courses.views import CourseViewSet

router = routers.DefaultRouter()

router.register("", CourseViewSet)

urlpatterns = router.urls
