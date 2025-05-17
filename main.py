from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Example", debug=True)


@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b


def main():
    print("Starting MCP server in stdio mode.")
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
