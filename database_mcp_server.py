from mcp.server.fastmcp import FastMCP
import json
from fastmcp.server.auth.providers.jwt import JWTVerifier
from fastmcp.server.auth import RemoteAuthProvider

jwtverifier = JWTVerifier(
    jwks_uri="your_jwks_uri",
    issuer="your_jwt_issuer",
    audience=["your_audience space_separated"]   # Custom audience for MCP server
)

auth = RemoteAuthProvider(
    token_verifier=jwtverifier,
    authorization_servers=[AnyHttpUrl("authorization_server_url")],
    base_url="http://localhost:8000"
)
mcp = FastMCP(name="MYDATABASE", auth=auth)

@mcp.tool()
def search(search_term: str, collection_name: str, authorization: str) -> str:
    """search for records using the search API on the database"""
    return "Records searched successfully"

@mcp.tool()
def store(record: json, collection_name: str, authorization: str) -> str:
    """Call Storage API on the database to ingest a record"""
    return "Record ingested successfully"

if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="localhost", port=8000,log_level="DEBUG")
