# Content Database MCP Workshop

This workshop will guide you through building an MCP server that helps you manage your content database in Notion.

We will cover the basics of setting up a Notion API integration, creating a basic MCP server, and implementing core functionality such as querying and creating entries in the database.

## Setup

If you don't have uv installed, you can install it using this command:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Make sure to restart your terminal afterwards to ensure that the uv command gets picked up.

Now, let’s create and set up our project:

```
# Create a new directory for our project
uv init content-database-mcp
cd content-database-mcp

# Create virtual environment and activate it
uv venv
source .venv/bin/activate

# Install dependencies
uv add "mcp[cli]" httpx

# Create our server file
touch main.py
```

Let's add the boilerplate code to main.py:

```python
from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("weather")

@mcp.tool()
async def my_tool() -> str:
    """My awesome tool."""
    print("I am going to do something awesome today!")

if __name__ == "__main__":
    # Initialize and run the server

    mcp.run(transport='stdio')
```

Let's run our server:

```bash
uv run main.py
```

This should output:

```bash
print("Starting MCP server...")
```

## Workshop Checkpoints

### Checkpoint 1: MCP Tool Design

1. Duplicate the following Notion Template in your workspace: [Content Database](https://www.notion.so/trillhouse/1c2e61f4e4968058a172e2267ec6b31e?v=1c2e61f4e496809382f1000c0aeec348)

2. Design the desired tools in our MCP server.

   - Find Posts
   - Create New Post
   - Add content to post

---

### Checkpoint 2: Notion API Integration

1. Create Notion API Token at [Notion Integrations](https://www.notion.so/profile/integrations)

2. Provide your integration access to the desired database.

3. Configure environment by adding an .env file:

   ```bash
   # .env file
   NOTION_TOKEN=your-notion-api-token
   ```

4. Install notion dependency:

   ```bash
   uv add notion-client
   ```

5. Code simple query to fetch all posts in the database.

_(Optional) Show how to test api calls ourside quickly_

---

### Checkpoint 3: Implement all the tools

1. Implement the `find_posts` tool to fetch posts from the database.

2. Implement the `create_post` tool to create a new post in the database.

3. Implement the `add_content_to_post` tool to add content to a post in the database.

4. Test the MCP server with an agent.
