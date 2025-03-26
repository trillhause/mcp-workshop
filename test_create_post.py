
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

def create_post(title: str, platform: str, status: str, tags: list[str], emoji: str): 
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

print(create_post(
    title="Hawaii Trip in Ghibli Style",
    platform="Twitter", 
    status="Idea",
    tags=["Travel", "Ghibli", "Hawaii", "Photography"],
    emoji="📝"
))