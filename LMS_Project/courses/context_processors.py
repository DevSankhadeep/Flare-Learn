from django.db.utils import OperationalError, ProgrammingError
from .models import Category

def courses_dropdown(request):
    """
    Add categories (with their related courses) to all templates.
    Safe: avoids crashing if migrations aren't applied or DB is unavailable.
    """
    categories = []
    try:
        categories = Category.objects.prefetch_related("courses").all()
    except (OperationalError, ProgrammingError):
        # Database not ready (e.g., before migrate) -> return empty list
        categories = []
    except Exception:
        # Catch-all fallback for unexpected errors
        categories = []

    return {"nav_categories": categories}
