from django.urls import path
from.import views

urlpatterns=[path("",views.home,name="home"),
             path("path1/",views.signup,name="signup"),
             path("path2/",views.login,name="login"),
             path("path3/",views.personal,name="personal"),
             path("path4/",views.personaldata,name="personaldata"),
             path("path5/",views.education,name="education"),
             path("path6/",views.educationdata,name="educationdata"),
             path("path7/",views.medical,name="medical"),
             path("path8/",views.medicaldata,name="medicaldata"),
             path("path9/",views.account,name="account"),
             path("path10/",views.accountdata,name="accountdata"),
             path("path11/",views.user_logout,name="user_logout"),
             path("path12/<id2>",views.personaledit,name="personaledit"),
             path("path13/<id1>",views.delete,name="delete"),
             path("path14/",views.culture,name="culture"),
             path("path15/",views.culturedata,name="culturedata"),
             path("path16/<id20>", views.accountedit, name="accountedit"),
             path("path17/<id25>", views.acdelete, name="acdelete"),
             path("path18/<id3>", views.educationedit, name="educationedit"),
             path("path19/<id8>", views.edudelete, name="edudelete"),
             path("path20/<id22>", views.cultureedit, name="cultureedit"),
             path("path21/<id12>", views.cultdelete, name="cultdelete"),
             path("path22/<id100>", views.medicaledit, name="medicaledit"),
             path("path23/<id99>", views.meddelete, name="meddelete"),
             path("path24/", views.aboutus, name="aboutus"),
             path("path25/", views.success, name="success"),
             path("path26/", views.invalid, name="invalid"),
             path("path27/", views.update, name="update"),
             path("path28/",views.profile,name="profile"),
             path("path29/",views.submit,name="submit"),
             path("path30/", views.deleted, name="deleted"),




             ]