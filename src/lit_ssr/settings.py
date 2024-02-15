host = 'http://localhost:3000'


def set_host(new_host):
    global host

    if new_host.endswith('/'):
        new_host = new_host[:-1]

    host = new_host
