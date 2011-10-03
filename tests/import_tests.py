from nose.tools import *

def loader(import_name, module_name):
    try:
        exec ("import " + import_name)
    except ImportError, e:
        print 'Error: your python installation is missing the %s module' % (module_name)
        return False
    return True

def pyyaml_test(): assert_equal(loader('yaml', 'PyYAML'), True)
def m2crypto_test(): assert_equal(loader('M2Crypto', 'M2Crypto'), True)
def crypto_test(): assert_equal(loader('Crypto.Cipher', 'pycrypto'), True)
def zmq_test(): assert_equal(loader('zmq', 'pyzmq'), True)
