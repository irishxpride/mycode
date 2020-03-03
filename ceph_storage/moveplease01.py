#!/usr/bin/python3

import shutil
import os
import sys

argv0= sys.argv[0]
argv1= sys.argv[1]
os.chdir('/home/student/mycode')
#shutil.move('raynor.obj', 'ceph_storage/')
#xname = input('What is the new name for kerrigan.obj? ')
#shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)
print(f"argv0 == {argv0}, argv1 == {argv1}")
