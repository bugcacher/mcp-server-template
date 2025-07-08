from mcp.server.fastmcp import FastMCP


def _register_greeting_tools(app: FastMCP):
    pass
    app.add_tool(say_hello, "say_hello")


def say_hello(name: str) -> str:
    return f"Hey, {name}!"
