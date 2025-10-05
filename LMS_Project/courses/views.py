from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, View
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

from .forms import SignUpForm, ProfileForm
from .models import Course, Category  # ✅ Include Category

# ✅ Home Page
class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["courses"] = Course.objects.all()[:6]  # show featured courses
        return context

# ✅ User Sign Up
class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})
        

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('login'))
        return render(request, 'registration/signup.html', {'form': form})

# ✅ Profile Update
@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(View):
    def get(self, request):
        p_form = ProfileForm(instance=request.user.profile)
        return render(request, 'courses/profile_update.html', {'p_form': p_form})

    def post(self, request):
        p_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            return redirect('profile_update')
        return render(request, 'courses/profile_update.html', {'p_form': p_form})

# ✅ Static Pages
class AboutPageView(TemplateView):
    template_name = "about.html"

class ContactPageView(TemplateView):
    template_name = "contact.html"

# ✅ Filtered Course List View
def filtered_course_list(request):
    courses = Course.objects.all()
    categories = Category.objects.all()

    course_type = request.GET.get("type")  # "free" or "paid"
    category_slug = request.GET.get("category")

    if course_type == "free":
        courses = courses.filter(price=0)
    elif course_type == "paid":
        courses = courses.exclude(price=0)

    if category_slug:
        courses = courses.filter(category__slug=category_slug)

    free_count = Course.objects.filter(price=0).count()
    paid_count = Course.objects.exclude(price=0).count()

    context = {
        "courses": courses,
        "categories": categories,
        "selected_type": course_type,
        "selected_category": category_slug,
        "free_count": free_count,
        "paid_count": paid_count,
    }

    return render(request, "courses/courses_list.html", context)

# ✅ Course Detail View
def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)

    template_map = {
        "fullstack-web-development": "courses/fullstack.html",
        "advanced-react-techniques": "courses/advanced-react.html",
        "python-for-beginners": "courses/python.html",
        "introduction-to-ui-design": "courses/ui-design.html",
        "html-for-beginners": "courses/html.html",
    }

    template_name = template_map.get(slug, "courses/course_detail.html")
    return render(request, template_name, {"course": course})
