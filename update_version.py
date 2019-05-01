# -*- coding: utf-8 -*-
import re

MAX = 100
def update_version():
    updated_content = None
    with open('setup.py', 'r', encoding='utf-8') as cfg:
        content = cfg.read()
        version_pattern = r'version\s*=\s*\"(\d+\.\d+\.\d+)\"'
        ret = re.search(version_pattern, content)
        if None != ret:
            old_version = ret.group(1)
            new_version = old_version.split('.')
            new_version[-1] = str(int(new_version[-1]) + 1)
            new_version = '.'.join(new_version)
            updated_content = content.replace(content[ret.start(1):ret.end(1)], new_version)
    
    if None != updated_content:
        with open('setup.py', 'w', encoding='utf-8') as cfg:
            cfg.write(updated_content)

if __name__ == '__main__':
    update_version()