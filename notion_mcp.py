from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("content-database-mcp")

@mcp.tool()
async def my_tool() -> str:
    """My awesome tool."""
    print("I am going to do something awesome today!")

if __name__ == "__main__":
    # Initialize and run the server
    print("Starting MCP server...")
    mcp.run(transport='stdio')