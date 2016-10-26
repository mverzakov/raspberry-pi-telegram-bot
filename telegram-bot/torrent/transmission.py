# -*- coding: utf-8 -*-
import subprocess
from .base import BaseTorrentConnector


class TransmissionConnector(BaseTorrentConnector):
    """Class is to interract with transmission torrent interface."""

    cmd = 'transmission-remote'

    def __init__(self, user='transmission', password='transmission'):
        self.auth_cmd = '-n {}:{}'.format(user, password)

    def run_cmd(self, params=[]):
        """Run torrent command."""
        command = [self.cmd, self.auth_cmd]
        command.extend(params)
        command = ' '.join(command)
        output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                                  stderr=subprocess.STDOUT)
        output = output.stdout.read().decode('utf-8')
        return '{0}'.format(output)

    def add_torrent(self, path_to_file, path_to_dir=None):
        params = ['-a {}'.format(path_to_file)]
        if path_to_dir:
            params.append('-w {}'.format(path_to_dir))
        return self.run_cmd(params)

    def torrents_list(self):
        """Return list of torrents."""
        return self.run_cmd(['-l'])

    def start(self, index):
        """Start specific torrents."""
        params = ['-t {}'.format(index), '-s']
        return self.run_cmd(params)

    def stop(self, index):
        """Stop specific torrents."""
        params = ['-t {}'.format(index), '-S']
        return self.run_cmd(params)

    def remove(self, index=None):
        """Remove specific torrents."""
        params = ['-t {}'.format(index), '-r']
        return self.run_cmd(params)
