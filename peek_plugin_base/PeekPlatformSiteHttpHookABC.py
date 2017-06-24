from abc import ABCMeta

from txhttputil.site.BasicResource import BasicResource
from txhttputil.site.FileUnderlayResource import FileUnderlayResource


class PeekPlatformSiteHttpHookABC(metaclass=ABCMeta):
    """ Peek Platform Site HTTP Hook

    The methods provided by this class apply to the HTTP sites served by the
    Client service for the mobile and desktop apps, and the Server service for the
    admin app.

    It is not the HTTP service that provides resources (vortex, etc) beween the server
    and the agent, worker and client.

    """
    def __init__(self):
        self.__rootSiteResource = FileUnderlayResource()

    def addSiteStaticResourceDir(self, dir: str) -> None:
        """ Add Site Static Resource Directory

        Calling this method sets up directory :code:`dir` to be served by the site.

        :param dir: The file system directory to be served.
        :return: None
        """
        self.__rootSiteResource.addFileSystemRoot(dir)

    def addSiteResource(self, pluginSubPath: bytes, resource: BasicResource) -> None:
        """ Add Site Resource

        Add a cusotom implementation of a served http resource.

        :param pluginSubPath: The resource path where you want to serve this resource.
        :param resource: The resource to serve.
        :return: None

        """
        pluginSubPath = pluginSubPath.strip(b'/')
        self.__rootSiteResource.putChild(pluginSubPath, resource)

    @property
    def rootSiteResource(self) -> BasicResource:
        """ Site Root Resource

        This returns the root site resource for this plugin.

        """
        return self.__rootSiteResource
