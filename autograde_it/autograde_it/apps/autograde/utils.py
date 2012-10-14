def create_repo():
    import requests
    response = requests.post("https://api.github.com/authorizations")
    return response

def extract_from_zip(file):
    import zipfile
    import os.path
    from readmeparser import parse
    from django.conf import settings
    z = zipfile.ZipFile(file)
    try:
        z.extractall(settings.AUTOGRADE_PROJECT_UPLOAD_PATH)
        parse(os.path.join(settings.AUTOGRADE_PROJECT_UPLOAD_PATH,"example_instructor_project"))
    except AttributeError:
        z.extractall("projects")

def run_test(submission,test_case):
    pass
