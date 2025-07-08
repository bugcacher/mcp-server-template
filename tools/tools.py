from mcp.server.fastmcp import FastMCP
from tools.greet import _register_greeting_tools


def register_tools(app: FastMCP):
    _register_greeting_tools(app)
