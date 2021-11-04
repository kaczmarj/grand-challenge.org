from django.contrib.auth.models import Group
from django.db import models
from django.utils import timezone
from guardian.shortcuts import assign_perm

from grandchallenge.core.storage import get_logo_path, get_pdf_path
from grandchallenge.subdomains.utils import reverse


class Company(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateField(default=timezone.now)
    company_name = models.CharField(max_length=200)
    website = models.URLField()
    founded = models.IntegerField()
    hq = models.CharField(max_length=100)
    email = models.EmailField()
    logo = models.ImageField(upload_to=get_logo_path, null=True,)
    description = models.TextField(
        blank=True, help_text="Short summary of this project.",
    )
    description_short = models.CharField(
        max_length=250,
        blank=True,
        help_text="Short summary of this project, max 250 characters.",
    )
    slug = models.SlugField()

    initial_editor = models.EmailField()
    editors_group = models.OneToOneField(
        Group,
        on_delete=models.PROTECT,
        editable=False,
        related_name="editors_of_company",
        null=True,
    )

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name_plural = "companies"
        ordering = ("pk",)

    def create_groups(self):
        self.editors_group = Group.objects.create(
            name=f"{self._meta.app_label}_{self._meta.model_name}_{self.pk}_editors"
        )

    def assign_permissions(self):
        # Allow the editors group to change, read and view this study
        assign_perm(
            f"change_{self._meta.model_name}", self.editors_group, self
        )
        assign_perm(f"read_{self._meta.model_name}", self.editors_group, self)
        assign_perm(f"view_{self._meta.model_name}", self.editors_group, self)

        # Allow readers and editors to add Products (globally)
        # adding them to this Company is checked in the serializers as
        # there is no get_permission_object in django rest framework.
        assign_perm(
            f"{Product._meta.app_label}.add_{Product._meta.model_name}",
            self.editors_group,
        )

        # BELOW NECESSARY?
        # reg_and_anon = Group.objects.get(
        #     name=settings.REGISTERED_AND_ANON_USERS_GROUP_NAME
        # )

        # if self.public:
        #     assign_perm(f"view_{self._meta.model_name}", reg_and_anon, self)
        # else:
        #     remove_perm(f"view_{self._meta.model_name}", reg_and_anon, self)

    def is_editor(self, user):
        """Checks if ``user`` is an editor for this ``Company``."""
        return user.groups.filter(pk=self.editors_group.pk).exists()

    def add_editor(self, user):
        """Adds ``user`` as an editor for this ``Company``."""
        return user.groups.add(self.editors_group)

    def remove_editor(self, user):
        """Removes ``user`` as an editor for this ``Company``."""
        return user.groups.remove(self.editors_group)

    # BELOW NECESSARY?
    def save(self, *args, **kwargs):
        adding = self._state.adding

        if adding:
            self.create_groups()

        super().save(*args, **kwargs)

        self.assign_permissions()

    # BELOW NECESSARY?
    # def delete(self):
    #     ct = ContentType.objects.filter(
    #         app_label=self._meta.app_label, model=self._meta.model_name
    #     ).get()
    #     Follow.objects.filter(object_id=self.pk, content_type=ct).delete()
    #     super().delete()

    def get_absolute_url(self):
        return reverse("products:company-detail", kwargs={"slug": self.slug})


class ProductImage(models.Model):
    img = models.ImageField(upload_to=get_logo_path)


class Status:
    CERTIFIED = "cer"
    YES = "yes"
    NO = "no"
    NA = "na"
    CLEARED = "cle"
    DE_NOVO_CLEARED = "dnc"
    PMA_APPROVED = "pma"
    UNKNOWN = "unk"


class Product(models.Model):
    class Verified(models.TextChoices):
        YES = Status.YES, "Yes"
        NO = Status.NO, "No"

    class CEStatus(models.TextChoices):
        CERTIFIED = Status.CERTIFIED, "Certified"
        NO = Status.NO, "No or not yet"
        NA = Status.NA, "Not applicable"
        UNKNOWN = Status.UNKNOWN, "Unknown"

    class FDAStatus(models.TextChoices):
        CLEARED = Status.CLEARED, "510(k) cleared"
        DE_NOVO_CLEARED = Status.DE_NOVO_CLEARED, "De novo 510(k) cleared"
        PMA_APPROVED = Status.PMA_APPROVED, "PMA approved"
        NO = Status.NO, "No or not yet"
        NA = Status.NA, "Not applicable"
        UNKNOWN = Status.UNKNOWN, "Unknown"

    ICONS = {
        Status.CERTIFIED: "icon_check.png",
        Status.YES: "icon_check.png",
        Status.NO: "icon_no.png",
        Status.NA: "icon_na.png",
        Status.CLEARED: "icon_check.png",
        Status.DE_NOVO_CLEARED: "icon_check.png",
        Status.PMA_APPROVED: "icon_check.png",
        Status.UNKNOWN: "icon_question.png",
    }

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateField(default=timezone.now)
    product_name = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    slug = models.SlugField()
    description = models.TextField(
        blank=True, help_text="Short summary of this project.",
    )
    description_short = models.CharField(
        max_length=250,
        default="",
        blank=True,
        help_text="Short summary of this project, max 250 characters.",
    )
    modality = models.CharField(max_length=100)
    subspeciality = models.CharField(max_length=300)
    diseases = models.TextField()
    population = models.TextField()

    input_data = models.CharField(max_length=250)
    file_format_input = models.TextField()
    output_data = models.CharField(max_length=250)
    file_format_output = models.TextField()
    key_features = models.TextField()
    key_features_short = models.CharField(max_length=120)
    software_usage = models.TextField()

    verified = models.CharField(
        choices=Verified.choices, max_length=3, default=Verified.NO
    )
    ce_status = models.CharField(
        choices=CEStatus.choices, max_length=3, default=CEStatus.NO
    )
    ce_under = models.CharField(max_length=10, blank=True)
    ce_class = models.CharField(max_length=500, default="unknown")
    fda_status = models.CharField(
        choices=FDAStatus.choices, max_length=3, default=FDAStatus.UNKNOWN
    )
    fda_class = models.CharField(max_length=500, default="unknown")
    ce_verified = models.CharField(
        choices=Verified.choices, max_length=3, default=Verified.NO
    )

    integration = models.TextField()
    deployment = models.TextField()
    process_time = models.TextField()
    trigger = models.CharField(max_length=200)

    market_since = models.TextField()
    countries = models.TextField()
    distribution = models.CharField(max_length=150, blank=True)
    institutes_research = models.TextField()
    institutes_clinic = models.TextField()

    pricing_model = models.TextField()
    pricing_basis = models.TextField()

    tech_papers = models.TextField()
    clin_papers = models.TextField()
    tech_peer_papers = models.TextField()
    tech_other_papers = models.TextField()
    all_other_papers = models.TextField()

    images = models.ManyToManyField(ProductImage)

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ("pk",)

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"slug": self.slug})


class EditorRequest(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class ProjectAirFiles(models.Model):
    title = models.CharField(max_length=150)
    study_file = models.FileField(upload_to=get_pdf_path)
    archive = models.BooleanField(
        default=False,
        help_text="Set to True if the file is no longer the most recent version. It will remain available on the page for download under archived protocols.",
    )
