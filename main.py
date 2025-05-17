from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Example", debug=True)


@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Adds two integers and returns the result.

    Args:
        a (int): The first integer to add.
        b (int): The second integer to add.

    Returns:
        int: The sum of the two integers.
    """
    return a + b


def main():
    print("Starting MCP server in stdio mode.")
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
