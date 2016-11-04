# -*- coding: utf-8 -*-
import transmissionrpc

from .base import BaseTorrentConnector


class TransmissionConnector(BaseTorrentConnector):
    """Class is to interract with transmission torrent interface."""

    def __init__(self, host='localhost', port=9091):
        self.client = transmissionrpc.Client(host, port=port)

    def add_torrent(self, path_to_file, path_to_dir=None):
        return self.add_torrent(path_to_file, paused=True)

    def torrents_list(self):
        """Return list of torrents."""i
        attrs=('id', 'name', 'status', 'percentDone', 'eta')
        return self.client.get_torrents(arguments=attrs)

    def start(self, index):
        """Start specific torrents."""
        return self.client.start_torrent(index)

    def stop(self, index):
        """Stop specific torrents."""
        return self.stop_torrent(index)

    def remove(self, index):
        """Remove specific torrents."""
        return self.remove_torrent(index, delete_data=True)
