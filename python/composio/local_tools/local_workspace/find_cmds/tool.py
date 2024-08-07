from composio.core.local import Tool
from composio.local_tools.local_workspace.find_cmds.actions import (
    FindFileCmd,
    SearchDirCmd,
    SearchFileCmd,
)


class SearchTool(Tool):
    """
    command manager tool for workspace
    """

    def actions(self) -> list:
        return [SearchDirCmd, SearchFileCmd, FindFileCmd]

    def triggers(self) -> list:
        return []
