from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from currency import views

urlpatterns = [
    path(
        "requestresponcelogs/list/",
        views.MiddlewareLogListView.as_view(),
        name="middlewarelog_list",
    ),
    path(
        "sources/delete/<int:pk>/",
        views.SourceDeleteView.as_view(),
        name="source_delete",
    ),
    path(
        "sources/update/<int:pk>/",
        views.SourceUpdateView.as_view(),
        name="source_update",
    ),
    path("sources/create/", views.SourceCreateView.as_view(), name="source_create"),
    path("sources/list/", views.SourcesListView.as_view(), name="sources_table"),
    path(
        "contacts/delete/<int:pk>/",
        views.ContactDeleteView.as_view(),
        name="contact_delete",
    ),
    path(
        "contacts/update/<int:pk>/",
        views.ContactUpdateView.as_view(),
        name="contact_update",
    ),
    path("contacts/create/", views.ContactCreateView.as_view(), name="contact_create"),
    path("contacts/list/", views.ContactsListView.as_view(), name="contacts_table"),
    path("rates/delete/<int:pk>/", views.RateDeleteView.as_view(), name="rate_delete"),
    path("rates/update/<int:pk>/", views.RateUpdateView.as_view(), name="rate_update"),
    path("rates/create/", views.RateCreateView.as_view(), name="rate_create"),
    path("rates/list/", views.RatesListView.as_view(), name="rates_table"),
    path("", views.HomeTemplateView.as_view(), name="home"),
]

# added for media files handling
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
