from pathlib import Path

from abc import abstractmethod
from txhttputil.site.BasicResource import BasicResource
from txhttputil.site.FileUnderlayResource import FileUnderlayResource

from peek_plugin_base.PeekPlatformCommonHookABC import PeekPlatformCommonHookABC
from peek_plugin_base.PeekPlatformFileStorageHookABC import PeekPlatformFileStorageHookABC
from peek_plugin_base.PeekPlatformServerHttpHookABC import PeekPlatformServerHttpHookABC
from peek_plugin_base.PeekPlatformSiteHttpHookABC import PeekPlatformSiteHttpHookABC


class PeekServerPlatformHookABC(PeekPlatformCommonHookABC,
                                PeekPlatformSiteHttpHookABC,
                                PeekPlatformServerHttpHookABC,
                                PeekPlatformFileStorageHookABC):

    @property
    @abstractmethod
    def dbConnectString(self) -> str:
        """ DB Connect String

        :return: The SQLAlchemy database engine connection string/url.

        """