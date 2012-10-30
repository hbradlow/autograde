from urllib import urlretrieve
from urllib2 import Request, build_opener, urlencode, urlopen
from json import loads, dumps
from os import mkdir, rmdir
from subprocess import Popen, PIPE, STDOUT
from getpass import getpass

class TestCase:
    def __init__(self, case_name, case_id):
        self.case_name = case_name
        self.case_id = case_id

    def runTest(self, timelimit=-1):
        print "Running test %i" % self.case_id
        p = Popen('.tests/'+self.case_name, stdout=PIPE, stderr=STDOUT)
        while True:
            retcode = p.poll()
            line = p.stdout.readline()
            yield line
            if retcode is not None:
                break

class Tester:
    def __init__(self, uname=None, api_key=None, server_url='http://autograde.herokuapp.com/'):
        self.key = api_key
        self.uname = uname
        self.url = server_url
        self.cases = []
        self.results = []
        self.api_url = 'autograde/api/data/project/1/?format=json'
        self.response_url = 'autograde/api/data/test_result/'

    def start(self):
        if self.uname is None:
            print "Ready to begin testing. Please enter your credentials."
            uname = raw_input('Username: ')
        if self.key is None:
            self.key = raw_input('API Key: ')
        print "Please press enter when you are ready to start the test."
        u_input = raw_input('=>')
        self.result_url += '&username=%s&api_key=%s' % (self.uname, self.key)
        if u_input is not '':
            self.getCases()

    def getCases(self):
        mkdir('.tests')
        req = Request(self.url)
        opener = build_opener()
        response = loads(opener.open(req).read())
        print "Downloading test cases..."
        for case in response['tests']:
            case_id  = case['id']
            media_url = self.url + case['my_file']
            case_name = media_url.split('/')[-1]
            name, obj = urlretrieve(media_url, '.tests/'+case_name)
            self.cases.append(TestCase(case_name, case_id))
            print "Got %s" % case_name
        print "Done\n"

    def runTests(self, cases):
        print "Running the test cases..."
        for test in self.cases:
            self.results.append((test.case_id, test.runTest()))

    def putResults(self, key):
        for r in self.results:
            payload = {'id':r[0], 'output':r[1]}
            request = Request(self.response_url, payload)
            print r

    def cleanup(self):
        rmdir('.tests')
        

if __name__ == '__main__':
    t = Tester()
    from sys import argv
    if len(argv) > 1:
        self.key = argv[1]
    t.start()
    t.putResults()
    t.cleanup()
    
