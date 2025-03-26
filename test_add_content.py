
from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
import os
from notion_client import Client
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()


notion = Client(auth=os.environ.get("NOTION_TOKEN"))
DATABASE_ID = "1c2e61f4e4968058a172e2267ec6b31e"

def create_block_object(content: str) -> dict[str, Any]:
    """Create a block object from content text that can be used when creating/updating pages.
    
    Args:
        content: The text content to include in the block.
        
    Returns:
        A dictionary representing a Notion block object with the content.
    """
    return {
        "object": "block",
        "type": "paragraph",
        "paragraph": {
            "rich_text": [{
                "type": "text",
                "text": {
                    "content": content,
                    "link": None
                },
                "annotations": {
                    "bold": False,
                    "italic": False,
                    "strikethrough": False,
                    "underline": False,
                    "code": False,
                    "color": "default"
                },
                "plain_text": content,
                "href": None
            }]
        }
    }


def add_content_to_post(page_id: str, content: str) -> str:
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

print(add_content_to_post(
    page_id="1c2e61f4e496811e8640f63ab6443baf",
    content="Just got back from an amazing trip to Hawaii! The lush landscapes and crystal clear waters reminded me of scenes straight out of a Ghibli film. Here are some photos I edited in that dreamy Ghibli style... 🌺✨"
))

