import os
import time
from concurrent import futures

import grpc

import services
from settings import *


def add_services(server):
    """
    add services
    :param server:
    :return:
    """
    for i in [i.split('.')[0] for i in os.listdir('services')]:
        __import__('services.%s' % i)

    for i in dir(services):
        if '__' in i:
            continue
        m = getattr(services, i)
        m0 = None
        m3 = None

        for ii in dir(m):
            if '__' in ii:
                continue
            k = 'Service'
            if k == ii[-(len(k)):]:
                m0 = getattr(m, ii)
            k = '_pb2_grpc'
            if k == ii[-(len(k)):]:
                m2 = getattr(m, ii)
                for iii in dir(m2):
                    if '__' in iii:
                        continue
                    if '_to_server' in iii:
                        m3 = getattr(m2, iii)
        m3(m0(), server)


def serve():
    """
    start server
    :return:
    """
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=MAX_WORKERS))
    add_services(server)
    server.add_insecure_port(HOST)
    server.start()
    print(f"host: {HOST}")
    try:
        while 1:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    """
    python3 grpc_server.py
    """
    serve()
