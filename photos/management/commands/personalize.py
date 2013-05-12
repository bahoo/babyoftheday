import os
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        child_name = raw_input("What is your child's name? ")
        author_name = raw_input("What is your (the author's) name? ")
        domain_name = raw_input("What domain will you be using? ")
        project_root = os.path.abspath(__file__ + "/../../../..")

        # write these to the project.py file
        project_file = open(project_root + "/settings/project.py", "w+b")
        project_file.writelines(["CHILD_NAME = \"%s\"\n" % child_name,
                                "AUTHOR_NAME = \"%s\"\n" % author_name,
                                "DOMAIN_NAME = \"%s\"\n" % domain_name,
                                "PROJECT_ROOT = \"%s\"\n" % project_root])
