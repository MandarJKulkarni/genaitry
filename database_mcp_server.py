from mcp.server.fastmcp import FastMCP
import json
mcp = FastMCP("MYDATABASE")

@mcp.tool()
def search(search_term: str, collection_name: str, authorization: str) -> str:
    """search for records using the search API on the database"""
    return "Records searched successfully"

@mcp.tool()
def store(record: json, collection_name: str, authorization: str) -> str:
    """Call Storage API on the database to ingest a record"""
    return "Record ingested successfully"

if __name__ == "__main__":
    mcp.run(transport="stdio")
