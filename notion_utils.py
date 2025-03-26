def create_block_object(content: str) -> dict:
    """Create a block object for Notion API.
    
    Args:
        content: The text content to add to the block
    
    Returns:
        A dictionary representing a Notion paragraph block
    """
    return {
        "object": "block",
        "type": "paragraph",
        "paragraph": {
            "rich_text": [
                {
                    "type": "text",
                    "text": {
                        "content": content
                    }
                }
            ]
        }
    } 