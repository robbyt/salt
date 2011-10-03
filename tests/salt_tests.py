import os, random
from nose.tools import *
from salt import salt

def clean_up_dir(d):
    if os.path.isdir(d): os.removedirs(d)

def verify_env_test():
    test_file = ['/tmp/' + str(random.getrandbits(10))]
    clean_up_dir(test_file[0])
    salt.verify_env(test_file)
    assert_equal(os.path.isdir(test_file[0]), True)
    clean_up_dir(test_file[0])

