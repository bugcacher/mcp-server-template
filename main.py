from mcp.server.fastmcp import FastMCP
from tools.tools import register_tools

app = FastMCP("app")

register_tools(app)

if __name__ == "__main__":
    app.run(transport="stdio")
