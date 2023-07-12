keepalive

Using keepalive
===============

Based on a stackoverflow post (https://stackoverflow.com/questions/12248132/how-to-change-tcp-keepalive-timer-using-python-script)

.. code-block:: python

    import socket, keepalive

    # keepalive.set(socket, after_idle_sec=60, interval_sec=60, max_fails=5)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    keepalive.set(client_socket)

Changelog
=========

0.0.1: initial release (2023-07-12)

