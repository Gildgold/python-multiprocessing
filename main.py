

import py_ecc
import random
import multiprocessing
import logging

def main():
    
    size = 8
    
    print "### Running test_pool with {} processes".format(size)
    p = multiprocessing.Pool(size)
    data = range(8)

    print data, "=>", p.map(worker, data)
    p.terminate()
    p.join()
    print ""

def worker(data):
    """
    This worker simply returns the square value.
    """
    return data*data

def enable_debug():
    """
    Enables the full debug, including for sub processes.
    """
    logger = multiprocessing.log_to_stderr(logging.DEBUG)
    logger.setLevel(multiprocessing.SUBDEBUG)



if __name__ == '__main__':
    main()