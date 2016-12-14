from typing import Optional

from peek_plugin_base.PluginCommonEntryHookABC import PluginCommonEntryHookABC
from peek_plugin_base.worker.PeekWorkerPlatformHookABC import PeekWorkerPlatformHookABC


class PluginAgentEntryHookABC(PluginCommonEntryHookABC):

    def __init__(self, pluginName: str, pluginRootDir: str, platform: PeekWorkerPlatformHookABC):
        PluginCommonEntryHookABC.__init__(self, pluginName=pluginName, pluginRootDir=pluginRootDir)
        self._platform = platform

    @property
    def publishedAgentApi(self, requestingPluginName:str) -> Optional[object]:
        return None
