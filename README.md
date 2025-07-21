# 🚀 mcp-server-template

This repository serves as a **template** for building MCP server projects in Python. You can use this repository as a starting point for your own server implementations by clicking "Use this template" on GitHub.

**Repository Reference:**  
[bugcacher/mcp-server-template](https://github.com/bugcacher/mcp-server-template)

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
