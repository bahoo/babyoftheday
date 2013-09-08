import os
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        child_name = raw_input("What is your child's name? ")
        domain_name = raw_input("What domain will you be using? ")
        author_name = raw_input("What is your (i.e. the author's) full name? ")
        author_email = raw_input("What is your (i.e. the author's) email? ")

        aws_access_key_id = raw_input("What is your Amazon access key? ")
        aws_secret_access_key = raw_input("What is your Amazon secret access key? ")

        project_root = os.getcwd()

        admin_username = author_name.split()[0].lower()

        # write these to the project.py file
        project_file = open(project_root + "/settings/project.py", "w+b")
        project_file.writelines(["CHILD_NAME = '%s'\n" % child_name,
                                "AUTHOR_NAME = '%s'\n" % author_name,
                                "DOMAIN_NAME = '%s'\n" % domain_name,
                                "PROJECT_ROOT = '%s'\n" % project_root,
                                "ADMIN_USERNAME = '%s'\n" % admin_username,
                                "ADMIN_EMAIL = '%s'\n\n" % author_email,
                                "AWS_ACCESS_KEY_ID = '%s'\n" % aws_access_key_id,
                                "AWS_SECRET_ACCESS_KEY = '%s'\n" % aws_secret_access_key,
                                "AWS_STORAGE_BUCKET_NAME = '%s'" % domain_name])

        print "\n\nproject.py successfully output to settings directory."