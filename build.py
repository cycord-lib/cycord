#!/opt/homebrew/bin/python3

import glob
import os
import shutil
import site
import subprocess

os.chdir('cycord_source')

if not os.path.exists('cycord_source'):
    os.mkdir('cycord_source')

shutil.copy('__init__.pyx', '__init__.pyx.bak')

lines = open("__init__.pyx").read().split("\n")

lines = [
    open(line.split("# content: ", 1)[1].strip()).read() if line.startswith("# content: ") else line
    for line in lines
]

open("__init__.pyx","w").write("\n".join(lines))

subprocess.run(['python3', 'setup.py', 'build_ext', '--inplace', '--build-lib=../'])

os.remove("__init__.pyx")
shutil.move('__init__.pyx.bak','__init__.pyx')

print("Cleaning up Cython generated files")
shutil.rmtree('build', ignore_errors=True)
for file in ['*.c', '*.so']:
    for f in glob.glob(file):
        os.remove(f)

os.rmdir("cycord_source")

os.chdir('Objects')
for file in glob.glob('*.c'):
    os.remove(file)

os.chdir('../..')

dest = site.getsitepackages()[0]

pyi_file = os.path.join('stub', 'cycord.pyi')

for file in glob.glob('*.so'):
    if 'cycord' in file:
        # Define the target filenames
        so_dest = os.path.join(dest, 'cycord.so')
        pyi_dest = os.path.join(dest, 'cycord.pyi')

        # Rename and copy the `.so` file
        print(f"Moved {file} -> {so_dest}")
        shutil.copy(file, so_dest)

        # Rename and copy the `.pyi` file
        if os.path.exists(pyi_file):
            print(f"Moved {pyi_file} -> {pyi_dest}")
            shutil.copy(pyi_file, pyi_dest)
        else:
            print(f"Stub file {pyi_file} not found.")