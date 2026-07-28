from dataclasses import dataclass,field
from typing import Callable,Any


@dataclass
class ToolEntry:
    name:str
    description:str
    parameters:dict
    handler:Callable

    category:str ="general"


class ToolRegistry:

    def __init__(self):
        self._tools = dict[str,ToolEntry]={}

    def register(self,name,description,parameters,handler,category="general"):
        self._tools[name]=ToolEntry(
            name=name,
            description=description,
            parameters=parameters,
            handler=handler,
            category=category
        )

    def get_schemas(self,categories=None):

        tools=self._tools.values()

        if categories:
            tools = [t for t in tools if t.category in categories]

        return [
            {
                "type":"function",
                "function":{
                    "name":t.name,
                    "description":t.description,
                    "parameters":t.parameters
                },
            }

            for t in tools
        ]

    def execute(self,name:str,args:dict)->str:
        entry = self._tools.get(name)

        if not entry:
            return f"Unknown tool name {name}"

        try:
            return entry.handler(**args)
        except Exception as e:
            return f"Error executing tool {name}: {str(e)}"


registry=ToolRegistry()
       