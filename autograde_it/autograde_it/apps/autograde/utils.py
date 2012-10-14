def create_repo():
    import requests
    response = requests.post("https://api.github.com/authorizations")
    return response

def extract_from_zip(file):
    import zipfile
    from django.conf import settings
    z = zipfile.ZipFile(file)
    try:
        z.extractall(settings.AUTOGRADE_PROJECT_UPLOAD_PATH)
    except AttributeError:
        z.extractall("projects")

def run_test(submission,test_case):
    pass
