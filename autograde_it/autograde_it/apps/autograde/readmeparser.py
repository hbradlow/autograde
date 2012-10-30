import re, os
from autograde.models import *
from django.core.files import File


def parse(directory):
    """
    Parses the README file and creates the required models
    """
    def flushBuffer(buf, results):
        results[current_header] = buf
        return [], results
    header_patt = r'-{5}-*([a-zA-Z]*)'
    results = {} # maps section names to a list containing the content from the section
    sections = ['description', 'dependencies', 'tests', 'verification', 'student']
    with open(directory+'/README.txt') as readme:
        print "parsing"
        section_buffer = []
        current_header = re.match(header_patt, readme.readline()).groups()[0]
        for line in readme:
            match = re.match(header_patt, line)
            if match:
                section_buffer, results = flushBuffer(section_buffer, results)
                current_header = match.groups()[0].lower()
                if current_header not in sections:
                    raise ValueError('Invalid header name: ' + current_header)
            else:
                section_buffer.append(line)
    section_buffer, results = flushBuffer(section_buffer, results)
    p = makeModels(results,directory)
    return p

def makeModels(readme_sections, root_dir):
    proj = Project()
    proj.save()
    def makeDescription():
        results = {}
        subsection_patt = r'^\s*#(.*)'
        subsection_buffer = []
        current_header = ''
        def flushSubsection(buf, results):
            if buf == []:
                return [], results
            else:
                results[current_header] = buf
                return [], results
        for line in readme_sections['description']:
            line = line.split('\n')[0]
            match = re.match(subsection_patt, line)
            if match:
                subsection_buffer, results = flushSubsection(subsection_buffer, results)
                current_header = match.groups()[0].lower()
            else:
                subsection_buffer.append(line)
        subsection_buffer, results = flushSubsection(subsection_buffer, results)
        for k,v in results.items():
            p = KVPair(key=k, value=v)
            p.save()
            proj.settings.add(p)

    def makeDependencies():
        for line in readme_sections['dependencies']:
            for direc in os.walk(root_dir+'/'+line):
                for f in direc[2]:
                    p = ProjectFile(file=file(f))
                    p.save()
                    proj.framework_files.add(p)
    
    def makeTests():
        # only working for single level directories
        for line in readme_sections['tests']:
            path = root_dir+'/'+line.split('\n')[0]
            for direc in os.walk(path):
                for f in direc[2]:
                    with open(path+'/'+f, 'rw') as g:
                        p = TestCase(my_file=File(g))
                        p.save()
                        proj.test_cases.add(p)

    def makeVerification():
        path = root_dir+'/'+readme_sections['verification'][0].split('\n')[0]
        with open(path) as f:
            p = ProjectFile(my_file=File(f))
            p.save()
            proj.verifer.add(p)

    def makeStudent():
        regex_patt = r'/(".*)'
        current_folder = ''
        for line in readme_sections['student']:
            match = re.search(regex_patt, line)
            if match:
                p = KVPair(key=current_folder, value=match.groups()[0])
                p.save()
                proj.student_files.add(p)
            else:
                current_folder = line

    makeDescription()
    makeDependencies()
    makeTests()
    makeVerification()
    makeStudent()
    proj.save()
    return proj
