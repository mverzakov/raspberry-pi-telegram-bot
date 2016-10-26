#!/bin/bash

echo Starting Transmission remote.

exec /usr/bin/transmission-daemon --foreground --config-dir /etc/transmission-daemon
