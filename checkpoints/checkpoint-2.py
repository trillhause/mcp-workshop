from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
import os
from notion_client import Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize FastMCP server
mcp = FastMCP("my-notion-mcp")
notion = Client(auth=os.environ.get("NOTION_TOKEN"))

DATABASE_ID = "<ADD_YOUR_DATABASE_ID>"

@mcp.tool()
async def find_posts() -> str:
    """Find posts in my content database."""
    print("Querying database for posts...")
    response = notion.databases.query(database_id=DATABASE_ID)
    return response

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
