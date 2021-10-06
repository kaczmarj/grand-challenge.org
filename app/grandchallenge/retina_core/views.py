import SimpleITK
from PIL import Image as PILImage
from django.conf import settings
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View
from rest_framework import status

from grandchallenge.cases.models import Image
from grandchallenge.retina_api.mixins import RetinaAPIPermissionMixin


class ThumbnailView(RetinaAPIPermissionMixin, View):
    """
    View class for returning a thumbnail of an image as png (max height/width: 128px)
    Currently, the thumbnail is created on the fly. Later this should be done on import.
    """

    raise_exception = True  # Raise 403 on unauthenticated request

    def get(self, request, image_id):
        image_object = get_object_or_404(Image, pk=image_id)

        if not request.user.has_perm("view_image", image_object):
            return HttpResponse(status=status.HTTP_403_FORBIDDEN)

        image_itk = image_object.get_sitk_image()
        if image_itk is None:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        depth = image_itk.GetDepth()
        image_nparray = SimpleITK.GetArrayFromImage(image_itk)
        if depth > 0:
            # Get middle slice of image if 3D
            image_nparray = image_nparray[depth // 2]
        image = PILImage.fromarray(image_nparray)
        image.thumbnail(
            (
                settings.RETINA_DEFAULT_THUMBNAIL_SIZE,
                settings.RETINA_DEFAULT_THUMBNAIL_SIZE,
            ),
            PILImage.ANTIALIAS,
        )
        response = HttpResponse(content_type="image/png")
        image.save(response, "png")
        return response
