import re, os
import models

def parse(directory):
    """
    Parses the README file and creates the required models
    """
    header_patt = r'-{5}-*([a-zA-Z]+)'
    results = {}
    sections = ['description', 'dependencies', 'tests', 'verfication', 'student']
    with open(directory+'/README.txt') as readme:
        section_buffer = []
        current_header = ''
        for line in readme:
            match = re.match(header_patt)
            if match:
                flushBuffer(section_buffer)
                current_header = match.groups()[0].lower()
                if current_header not in sections:
                    raise ValueError('Invalid header name')
            else:
                section_buffer.append(line)
    return makeModels(results, directory)
    def flushBuffer(buf):
        if buf == '':
            pass
        results[current_header] = buf
        section_buffer = []

def makeModels(readme_sections, root_dir):
    proj = Project()
    def makeDescription():
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
        def flushSubsection(buf):
            if buf == '':
                pass
            results[current_header] = buf
        for k,v in results.items():
            proj.settings.add(KVPair(key=k, value=v))

    def makeDependencies():
        for line in readme_sections['dependencies']:
            for direc in os.walk(root_dir+'/'+line)
                for f in direc[2]:
                    p = ProjectFile(file=file(f))
                    proj.framework_files.add(p)
    
    def makeTests():
        for line in readme_sections['tests']:
            for direc in os.walk(root_dir+'/'+line):
                for f in direc[2]:
                    p = TestCase(file=file(f))
                    proj.test_cases.add(p)

    def makeVerification():
        path = root_dir+'/'+readme_sections['verification']
        p = TestCase(file=file(path))
        proj.test_cases.add(p)

    def makeStudent():
        regex_patt = r'/(".*)'
        current_folder = ''
        for line in readme_sections['student']:
            match = re.search(regex_patt, line)
            if match:
                proj.student_files.add(KVPair(key=current_folder, value=match.groups()[0]))
            else:
                current_folder = line

    makeDescription()
    makeDependencies()
    makeTests()
    makeVerification()
    makeStudent()
    return True

        
