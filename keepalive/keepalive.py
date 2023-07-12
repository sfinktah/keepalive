import socket
import platform

def set_keepalive_linux(sock, after_idle_sec, interval_sec, max_fails):
    """Set TCP keepalive on an open socket.

    It activates after 1 second (after_idle_sec) of idleness,
    then sends a keepalive ping once every 3 seconds (interval_sec),
    and closes the connection after 5 failed ping (max_fails), or 15 seconds
    """
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, after_idle_sec)
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, interval_sec)
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPCNT, max_fails)

def set_keepalive_osx(sock, after_idle_sec, interval_sec, max_fails):
    """Set TCP keepalive on an open socket.

    sends a keepalive ping once every 3 seconds (interval_sec)
    """
    # scraped from /usr/include, not exported by python's socket module
    TCP_KEEPALIVE = 0x10
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    sock.setsockopt(socket.IPPROTO_TCP, TCP_KEEPALIVE, interval_sec)

def set_keepalive_win(sock, after_idle_sec, interval_sec, max_fails):
    sock.ioctl(socket.SIO_KEEPALIVE_VALS, (1, after_idle_sec * 1000, interval_sec * 1000))


def set(sock, after_idle_sec=60, interval_sec=60, max_fails=5):
    plat = platform.system()
    if plat == 'Linux':
        return set_keepalive_linux(sock, after_idle_sec, interval_sec, max_fails)
    if plat == 'Darwin':
        return set_keepalive_osx(sock, after_idle_sec, interval_sec, max_fails)
    if plat == 'Windows':
        return set_keepalive_win(sock, after_idle_sec, interval_sec, max_fails)
    raise RuntimeError('Unsupport platform {}'.format(plat))
