# -*- coding: utf-8 -*-
"""Module contains base connector to torrent program."""
import abc
import six


@six.add_metaclass(abc.ABCMeta)
class BaseTorrentConnector(object):
    """Class is base connector to interact wit torrent."""

    @abc.abstractmethod
    def add_torrent(self, *args, **kwargs):
        """Add torrent."""

        pass

    @abc.abstractmethod
    def torrents_list(self, *args, **kwargs):
        """Return list of torrents."""

        pass

    @abc.abstractmethod
    def start(self, *args, **kwargs):
        """Start all torrents or specific."""

        pass

    @abc.abstractmethod
    def stop(self, *args, **kwargs):
        """Start all torrents or specific."""

        pass

    @abc.abstractmethod
    def remove(self, *args, **kwargs):
        """Remove all torrents or specific."""

        pass
