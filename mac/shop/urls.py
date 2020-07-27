from django.urls import path ,include
from . import views
urlpatterns = [
    path("",views.index,name="ShopHome"),
    path("Aboutus/",views.about_us,name="Aboutus"),
    path("contact/",views.contact,name="contact"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("checkout/",views.checkout,name="checkout"),
    path("tracker/",views.tracker,name="tracker"),
    path("search/",views.search,name="search"),
    path("register/",views.register,name="register"),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
    path("", include("django.contrib.auth.urls")),

]