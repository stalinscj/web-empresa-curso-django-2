from django.urls import path
from . import views

urlpatterns = [
	path('<int:page_id>/<slug:page_title>', views.page, name="page")
]

# pages_patterns =5