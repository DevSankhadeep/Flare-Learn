from django.urls import path
from .views import (
    HomePageView,
    SignUpView,
    ProfileUpdateView,
    AboutPageView,
    ContactPageView,
    filtered_course_list,  # ✅ use new view
    course_detail,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    

    # ✅ Courses
    path('courses/', filtered_course_list, name='course_list'),
    path('courses/<slug:slug>/', course_detail, name='course_detail'),
]
