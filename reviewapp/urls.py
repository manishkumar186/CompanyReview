from django.urls import path
from . import views


app_name="reviewapp"
urlpatterns = [
    path("",views.home,name="home"),
    path("detail/<int:id>/",views.detail,name="detail"),
    path("addcompany/",views.addcompany,name="addcompany"),
    path("editcompany/<int:id>/",views.editcompany,name="editcompany"),
    path("deletecompany/<int:id>/",views.deletecompany,name="deletecompany"),
    path("addreview/<int:id>/",views.addreview,name="addreview"),
    path("editreview/<int:company_id>/<int:review_id>/",views.editreview,name="editreview"),
    path("deletereview/<int:company_id>/<int:review_id>/",views.deletereview,name="deletereview")

]