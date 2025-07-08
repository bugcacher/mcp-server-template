from mcp.server.fastmcp import FastMCP


def _register_greeting_tools(app: FastMCP):
    pass
    app.add_tool(say_hello, "say_hello")


def say_hello(name: str) -> str:
    """
    Generate a personalized greeting message.

    This function is intended to be used as an MCP server tool to greet users by name.

    Args:
        name (str): The name of the person to greet.

    Returns:
        str: A greeting message addressed to the specified user.
    """
    return f"Hey, {name}!"
