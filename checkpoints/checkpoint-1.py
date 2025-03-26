from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("my-notion-mcp")

@mcp.tool()
async def find_posts() -> str:
    """Find posts in my content database."""
    print("Querying database for posts...")
    return ["Mock post 1", "Mock post 2", "Mock post 3"]

@mcp.tool()
async def create_post() -> str:
    """Create a new post in my content database."""
    print("Creating new post in database...")
    return "New mock post Created: New post title"

@mcp.tool()
async def add_content_to_post() -> str:
    """Update a database entry in Notion."""
    print("Adding content to post...")
    return "Content added to post"

if __name__ == "__main__":
    # Initialize and run the server
    print("Starting MCP server...")
    mcp.run(transport='stdio')


