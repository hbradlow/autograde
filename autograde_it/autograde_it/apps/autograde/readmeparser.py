import re, os
from autograde.models import *


def parse(directory):
    """
    Parses the README file and creates the required models
    """
    def flushBuffer(buf):
        if buf == '':
            pass
        results[current_header] = buf
        section_buffer = []
    header_patt = r'-{5}-*([a-zA-Z]+)'
    results = {}
    sections = ['description', 'dependencies', 'tests', 'verification', 'student']
    with open(directory+'/README.txt') as readme:
        section_buffer = []
        current_header = ''
        for line in readme:
            match = re.match(header_patt,line)
            if match:
                flushBuffer(section_buffer)
                current_header = match.groups()[0].lower()
                if current_header not in sections:
                    raise ValueError('Invalid header name: ' + current_header)
            else:
                section_buffer.append(line)
    return makeModels(results, directory)

def makeModels(readme_sections, root_dir):
    proj = Project()
    proj.save()
    def makeDescription():
        def flushSubsection(buf):
            if buf == '':
                pass
            results[current_header] = buf
            for k,v in results.items():
                proj.settings.add(KVPair(key=k, value=v))
        results = {}
        subsection_patt = r'^\s*#(.*)'
        subsection_buffer = ''
        current_header = ''
        for line in readme_sections['description']:
            match = re.match(subsection_patt, line)
            if match:
                flushSubsection(subsection_buffer)
                current_header = match.groups()[0].lower()
            else:
                subsection_buffer += line + '\n'

    def makeDependencies():
        for line in readme_sections['dependencies']:
            for direc in os.walk(root_dir+'/'+line):
                for f in direc[2]:
                    p = ProjectFile(file=file(f))
                    p.save()
                    proj.framework_files.add(p)
    
    def makeTests():
        for line in readme_sections['tests']:
            for direc in os.walk(root_dir+'/'+line):
                for f in direc[2]:
                    p = TestCase(file=file(f))
                    p.save()
                    proj.test_cases.add(p)

    def makeVerification():
        path = root_dir+'/'+readme_sections['verification']
        p = TestCase(file=file(path))
        p.save()
        proj.test_cases.add(p)

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
    return True

        
