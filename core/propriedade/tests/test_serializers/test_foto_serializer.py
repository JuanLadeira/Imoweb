import io

import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image

from core.propriedade.api.serializers.foto_serializer import FotoPostSerializer


@pytest.mark.django_db()
class TestFotoSerializer:
    def test_create_foto_post_serializer(self, imovel_factory, foto_factory):
        imovel = imovel_factory()

        image = Image.new("RGB", (100, 100), color="red")
        image_io = io.BytesIO()
        image.save(image_io, format="JPEG")
        image_io.seek(0)

        image_file = SimpleUploadedFile(
            name="test_image.jpg",
            content=image_io.read(),
            content_type="image/jpeg",
        )

        data = {
            "imovel": imovel.id,
            "foto": image_file,
        }

        serializer = FotoPostSerializer(data=data)
        assert serializer.is_valid(), serializer.errors
        foto = serializer.save()
        assert foto, serializer.errors
        assert foto.imovel == imovel, "deveria ser igual"
