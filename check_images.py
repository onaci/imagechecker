#!/bin/python

import os
from subprocess import Popen, PIPE, call
import sys
import yaml

debug = False
if '--debug' in sys.argv:
    debug = True
registry=os.getenv('REGISTRY')

cachefile='.reg_cache'
if os.path.isfile(cachefile):
    reg_cache = yaml.load(open(cachefile, 'r'))
else:
    reg_cache = dict()

def getInfo(image, cmd):
    if not image in reg_cache:
        reg_cache[image] = dict()
    if not cmd in reg_cache[image]:
        p = Popen("reg %s %s"%(cmd, image) , shell=True, stdout=PIPE, stderr=PIPE)
        out, err = p.communicate()
        #print "Return code: ", p.returncode
        #print out.rstrip()
        #print err.rstrip()
        reg_cache[image][cmd] = out.decode().rstrip().split("\n")
    return reg_cache[image][cmd]

def check_images():
    for filename in os.listdir('.'):
        if filename.endswith(".yml") and not filename.startswith('.'):
            try:
                y = yaml.load(open(filename, 'r'))
            except:
                print("SKIPPING %s"%filename)
                continue
            
            if 'services' in y:
                for k in y['services']:
                    s = y['services'][k]
                    if 'image' in s:
                        i = s['image']
                        i = i.replace('${REGISTRY}', registry)

                        if i.endswith(':latest'):
                            if debug:
                                print("\tOK: %s: %s: %s uses :latest"%(filename, k, i))
                            continue

                        parts=i.split('/')
                        name=parts[-1]
                        tag='latest'
                        if ':' in parts[-1]:
                            p = parts[-1].split(':')
                            name=p[0]
                            tag=p[1]

                        currentSHA = getInfo(i, 'digest')
                        tags = getInfo(i, 'tags')
                        parts[-1] = name+':latest'
                        latest = "/".join(parts)
                        latestSHA = getInfo(latest, 'digest')

                        if latestSHA[0] == '' and 'latest' in tags:
                            print("\tWARNING: %s has no digest"%latest)

                        if currentSHA[0] == latestSHA[0]:
                            if debug:
                                print("\tOK: %s: %s: %s has same digest as latest tag"%(filename, k, i))
                            continue
                        
                        print("%s\t\t%s"% (i, tags[-5:]))


# yes, you need https://github.com/genuinetools/reg in your path
p = Popen("reg version" , shell=True, stdout=PIPE, stderr=PIPE)
out, err = p.communicate()
if err.decode()!= '':
    print
    print("ERROR: need to install https://github.com/genuinetools/reg in PATH")
    print("       %s"%(err))
    exit
else:
    try:
        check_images()
    except BaseException as e:
        print("stopping: ")
        print(e)

    f = open(cachefile, 'w' )
    f.write(yaml.dump(dict(reg_cache)))
    f.close()
