# 🚀 mcp-server-template

A lightweight template to kickstart your MCP server project.

---

## Initialize your app with [uv](https://github.com/astral-sh/uv)

```bash
uv init .
```

## Install basic dependencies
```base
uv add "mcp[cli]"
uv add requests
```

## Add MCP tools to your project
```bash
uv run mcp install main.py
```

## Run the MCP server
You can run it directly from your favorite code editor, or use:

```bash
uv run mcp run main.py
```
