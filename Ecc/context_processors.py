from Ecc.models import Categories  # Example model
from django.contrib.auth.models import User

def navbar_data(request):
    categories = Categories.objects.all()  # Example: Fetch categories for navbar
#     user = request.user if request.user.is_authenticated else None

    return {
        "categories": categories,
        # "current_user": user,
    }