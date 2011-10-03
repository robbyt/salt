from nose.tools import *
from salt import salt

def verify_env_test():
#    pass
    salt.verify_env('tmp')
