from allauth.account.forms import SignupForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelChoiceField
from django.utils.safestring import mark_safe
from django_select2.forms import Select2MultipleWidget
from guardian.shortcuts import get_objects_for_user

from grandchallenge.blogs.forms import PostUpdateForm
from grandchallenge.core.forms import SaveFormInitMixin
from grandchallenge.core.templatetags.remove_whitespace import oxford_comma
from grandchallenge.policies.models import Policy
from grandchallenge.products.models import EditorRequest, ProjectAirFiles
from grandchallenge.uploads.models import UserUpload
from grandchallenge.uploads.widgets import UserUploadSingleWidget


class ImportForm(SaveFormInitMixin, forms.Form):
    products_file = ModelChoiceField(
        queryset=None, widget=UserUploadSingleWidget(),
    )
    companies_file = ModelChoiceField(
        queryset=None, widget=UserUploadSingleWidget(),
    )
    images_zip = ModelChoiceField(
        queryset=None, widget=UserUploadSingleWidget(),
    )

    def __init__(self, *args, user, **kwargs):
        super().__init__(*args, **kwargs)

        qs = get_objects_for_user(
            user, "uploads.change_userupload", accept_global_perms=False
        ).filter(status=UserUpload.StatusChoices.COMPLETED)

        for field in ["products_file", "companies_file", "images_zip"]:
            self.fields[field].queryset = qs


class ProductsSignupForm(SignupForm):
    accept_terms = forms.BooleanField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # mark_safe ok here as we control the policy page titles
        self.fields["accept_terms"].label = mark_safe(
            "I have read and agree to {}.".format(
                oxford_comma(
                    [
                        f'the <a href="{p.get_absolute_url()}">{p.title}</a>'
                        for p in Policy.objects.all()
                    ]
                )
            )
        )

    class Meta:
        model = get_user_model()
        fields = (
            "first_name",
            "last_name",
        )


class EditorRequestForm(SaveFormInitMixin, forms.ModelForm):
    def __init__(self, *args, company=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit("save", "Save and send e-mail"))

    class Meta:
        model = EditorRequest
        fields = ["name", "email"]


class ProjectAirFilesForm(SaveFormInitMixin, forms.ModelForm):
    class Meta:
        model = ProjectAirFiles
        fields = ["title", "study_file", "archive"]


class ProductsPostUpdateForm(PostUpdateForm):
    class Meta(PostUpdateForm.Meta):
        fields = (*PostUpdateForm.Meta.fields, "companies")
        widgets = {
            **PostUpdateForm.Meta.widgets,
            "companies": Select2MultipleWidget,
        }
