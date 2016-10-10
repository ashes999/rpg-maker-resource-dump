import fnmatch
import os
import sys

TEMPLATE_FILE = 'template.html'
OUTPUT_FILE = 'index.html'
PLACEHOLDER = '<resources />'

def list_files(dir, pattern):
    matches = []
    for root, dirnames, filenames in os.walk(dir):
        for filename in fnmatch.filter(filenames, pattern):
            matches.append(os.path.join(root, filename))
    return matches

files = list_files(os.curdir, "*.png")

html = '<ul>'

for filename in files:
    display_url = filename[2:] # trim ./
    html = html + "<li><a href='{0}'>{1}</a></li>".format(filename, display_url)
    
html += '</ul>'
f = open(TEMPLATE_FILE, 'r')
template = f.read().strip()
f.close()

template = template.replace(PLACEHOLDER, html)

f = open(OUTPUT_FILE, 'w')
f.write(template)
f.close()

print("Generated {0} with {1} links".format(OUTPUT_FILE, len(files)))
