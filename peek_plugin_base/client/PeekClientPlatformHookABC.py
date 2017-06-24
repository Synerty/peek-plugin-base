from peek_plugin_base.PeekPlatformCommonHookABC import PeekPlatformCommonHookABC
from peek_plugin_base.PeekPlatformFileStorageHookABC import PeekPlatformFileStorageHookABC
from peek_plugin_base.PeekPlatformServerInfoHookABC import PeekPlatformServerInfoHookABC
from peek_plugin_base.PeekPlatformSiteHttpHookABC import PeekPlatformSiteHttpHookABC


class PeekClientPlatformHookABC(PeekPlatformCommonHookABC,
                                PeekPlatformSiteHttpHookABC,
                                PeekPlatformServerInfoHookABC,
                                PeekPlatformFileStorageHookABC, ):
    pass
