from django.urls import path

from grandchallenge.products.views import (
    AboutPage,
    CompanyDetail,
    CompanyList,
    ContactPage,
    EditorRequestForm,
    EmailPage,
    ImportDataView,
    LogInPage,
    LogOutPage,
    PasswordChangePage,
    PasswordResetFromKeyPage,
    PasswordResetPage,
    ProductDetail,
    ProductList,
    ProductsPostCreate,
    ProductsPostDetail,
    ProductsPostList,
    ProductsPostUpdate,
    ProjectAirForm,
    ProjectAirPage,
    SignUpNotFoundPage,
    SignUpPage,
)

app_name = "products"

urlpatterns = [
    path("", ProductList.as_view(), name="product-list"),
    path("companies/", CompanyList.as_view(), name="company-list"),
    path("about/", AboutPage.as_view(), name="about"),
    path("contact/", ContactPage.as_view(), name="contact"),
    path("project-air/", ProjectAirPage.as_view(), name="project-air"),
    path("product/<slug>/", ProductDetail.as_view(), name="product-detail"),
    path("company/<slug>/", CompanyDetail.as_view(), name="company-detail"),
    path(
        "company/<slug>/editor-request/",
        EditorRequestForm.as_view(),
        name="editor-request",
    ),
    path("import-data/", ImportDataView.as_view(), name="import-data"),
    path(
        "project-air-files/",
        ProjectAirForm.as_view(),
        name="project-air-files",
    ),
    path("blogs/", ProductsPostList.as_view(), name="blogs-list"),
    path("blogs/create/", ProductsPostCreate.as_view(), name="blogs-create"),
    path("blogs/<slug>/", ProductsPostDetail.as_view(), name="blogs-detail"),
    path(
        "blogs/<slug>/update/",
        ProductsPostUpdate.as_view(),
        name="blogs-update",
    ),
    path("logout/", LogOutPage.as_view(), name="account_logout"),
    path("login/", LogInPage.as_view(), name="account_login"),
    path("signup/", SignUpPage.as_view(), name="account_signup"),
    path(
        "signup-not-found/",
        SignUpNotFoundPage.as_view(),
        name="account_signup_not_found",
    ),
    path(
        "password-change/",
        PasswordChangePage.as_view(),
        name="account_change_password",
    ),
    path(
        "password-reset-from-key/",
        PasswordResetFromKeyPage.as_view(),
        name="account_reset_password_from_key",
    ),
    path(
        "password-reset/",
        PasswordResetPage.as_view(),
        name="account_reset_password",
    ),
    path("email/", EmailPage.as_view(), name="account_email"),
]
