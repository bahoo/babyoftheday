from django.conf import settings


def project_variables(request):
    return {'CHILD_NAME': settings.CHILD_NAME,
            'AUTHOR_NAME': settings.AUTHOR_NAME}
