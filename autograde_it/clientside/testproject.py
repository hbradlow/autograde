from urllib import urlretrieve
from urllib2 import Request, build_opener, urlopen
from json import loads, dumps
from os import mkdir, rmdir
from subprocess import Popen, PIPE, STDOUT
from getpass import getpass
from shutil import rmtree
from uuid import uuid4

class TestCase:
    def __init__(self, case_name, case_id, test_dir, user_uri='autograde/api/data/user/1', resource_uri=''):
        self.case_name = case_name
        self.case_id = case_id
        self.test_dir = test_dir
        self.user_uri = user_uri
        self.resource_uri = resource_uri

    def runTest(self, timelimit=-1):
        print "Running test " + str(self.case_id)
        print self.test_dir+'/'+self.case_name
        filename = self.test_dir+'/'+self.case_name
        c = Popen('chmod +x '+filename, shell=True)
        p = Popen('python ' + filename, shell=True, stdout=PIPE, stderr=STDOUT)
        result = ''
        while True:
            retcode = p.poll()
            line = p.stdout.readline()
            result += line
            if retcode is not None:
                break
        self.result = result

    def asDict(self):
        return {'results':self.result, 'user':self.user_uri, 'test_case':self.resource_uri}

class Tester:
    '''
    Framework for testing a particular project, for a particular user.
    '''
    def __init__(self, uname='will', api_key='8a3cc5b747e93699f33beb4e250e3e47c4f8df05', server_url='http://autograde.herokuapp.com/'):
        self.key = api_key
        self.uname = uname
        self.url = server_url
        self.cases = []
        self.results = []
        self.api_url = self.url + 'autograde/api/data/project/?format=json'
        self.response_url = server_url + 'autograde/api/data/test_result/'
        self.user_uri_url = 'autograde/api/data/user/?format=json&username=%s' % self.uname
        self.test_dir = ''
        self.user_uri = ''

    def start(self):
        if self.uname is None:
            print "Ready to begin testing. Please enter your credentials."
            self.uname = raw_input('Username: ')
        if self.key is None:
            self.key = raw_input('API Key: ')
        print "Please press enter when you are ready to start the test."
        u_input = raw_input('=>')
        self.response_url += '?username=%s&api_key=%s' % (self.uname, self.key)
        self.test_dir = '.%stest' % self.uname
        self.getCases()

    def getCases(self):
        try:
            rmtree(self.test_dir)
        except:
            pass
        mkdir(self.test_dir)
        req = Request(self.api_url)
        opener = build_opener()
        response = opener.open(req).read()
        print response
        print self.url
        response_json = loads(response)
        print response_json
        print "Downloading test cases..."
        tests = response_json['objects'][1]['tests']
        print tests
        for case in tests:
            case_id  = case['id']
            media_url = case['file']
            resource_uri = case['resource_uri']
            print media_url
            case_name = str(uuid4())
            name, obj = urlretrieve(media_url, self.test_dir+'/'+case_name)
            self.cases.append(TestCase(case_name, case_id, self.test_dir, self.getUserUri(), resource_uri))
            print "Got %s" % case_name
        print "Done\n"

    def getUserUri(self):
        request = Request(self.url+self.user_uri_url)
        opener = build_opener()
        response = loads(opener.open(request).read())
        return response['objects'][0]['resource_uri']


    def runTests(self):
        print "Running the test cases..."
        for test in self.cases:
            test.runTest()

    def putResults(self, key):
        for test in self.cases:
            payload = dumps(test.asDict())
            print payload, self.response_url
            request = Request(self.response_url)
            response = urlopen(request, payload)

    def cleanup(self):
        rmtree(self.test_dir)
        

if __name__ == '__main__':
    t = Tester()
    from sys import argv
    if len(argv) > 1:
        self.key = argv[1]
    t.start()
    t.runTests()
    t.putResults(t.key)
    t.cleanup()
    
