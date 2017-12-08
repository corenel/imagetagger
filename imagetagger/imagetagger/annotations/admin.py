from django.contrib import admin

from .models import (Annotation, AnnotationType, Export,
                     Verification, ExportFormat)

admin.site.register(Annotation)
admin.site.register(AnnotationType)
admin.site.register(Export)
admin.site.register(Verification)
admin.site.register(ExportFormat)
