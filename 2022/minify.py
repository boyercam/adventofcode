import os
import re

def minify(code:str)->str:
    code = re.sub('#.*','', code)
    code = re.sub('\\s*([-+*/:=,])\\s*','\\1', code)
    code = re.sub('\\s*\n\\s*','', code)
    # TODO 2:1 or 3:1 packer if gain can be made

    return code


excludes = ['minify.py']

for file in os.listdir('.'):
    if file.endswith('.py') and not file.endswith('.min.py') and file not in excludes:
        with open(file[:-3]+'.min.py','w') as f:
            f.write(minify(open(file).read()))