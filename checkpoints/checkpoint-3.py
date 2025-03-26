from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
import os
from notion_client import Client
from dotenv import load_dotenv
from notion_utils import create_block_object
# Load environment variables from .env file
load_dotenv()

# Initialize FastMCP server
mcp = FastMCP("my-notion-mcp")
notion = Client(auth=os.environ.get("NOTION_TOKEN"))

DATABASE_ID = "<ADD_YOUR_DATABASE_ID>"

@mcp.tool()
async def find_posts(platform: str) -> str:
    """Find posts in my content database.
    
    Args:
        platform: The platform the post is supposed to be published on. Value must be "Twitter", "LinkedIn", "Blog".
    """
    print("Querying database for posts...")
    response = notion.databases.query(
        database_id=DATABASE_ID,
        filter={
            "property": "Platform",
            "select": {
                "equals": post_type
            }
        }
    )
    return response

@mcp.tool()
async def create_post(title: str, platform: str, status: str, tags: list[str], emoji: str) -> str:
    """Create a new post in my content database.
    
    Args:
        title: The title of the post.
        post_type: The type of post to create. Value must be "Twitter", "LinkedIn", "Blog".
        status: The status of the post. Value must be "Idea", "Draft", "In Review", "Published".
        tags: A list of tags for the post.
        emoji: The emoji to use for the post.
    """
    print("Creating new post in database...")

    ## Properties for new page
    new_page = {
        "Name": {"title": [{"text": {"content": title}}]},
        "Tags": {"type": "multi_select", "multi_select": [{"name": tag} for tag in tags]},
        "Platform": {"select": {"name": platform}},
        "Status": {"status": {"name": status}}
    }

    ## Icon for new page
    icon = {"type": "emoji", "emoji": emoji}
    
    # Create a new page in the database
    response = notion.pages.create(
        parent={
            "database_id": DATABASE_ID
        },
        icon=icon,
        properties=new_page
    )
    
    return response


@mcp.tool()
async def add_content_to_post(id: str, content: str) -> str:
    """Update a database entry in Notion.
    
    Args:
        page_id: The page_id of the post to add content to.
        content: The content to add to the post.
    """
   
    kwargs = {
        "children": [create_block_object(content)]
    }

    # Create a new page in the database
    response = notion.blocks.children.append(
        block_id=page_id,
        **kwargs
    )
    
    return response


if __name__ == "__main__":
    # Initialize and run the server
    print("Starting MCP server...")
    mcp.run(transport='stdio')
