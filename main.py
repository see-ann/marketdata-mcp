import uvicorn
from mcp.server.fastmcp import FastMCP
from starlette.middleware.cors import CORSMiddleware

mcp = FastMCP("MarketData")


@mcp.tool()
def get_stock_price(symbol: str) -> dict:
    """Get current stock price for a symbol."""
    return {"symbol": symbol, "price": 150.00, "currency": "USD"}


# Get the HTTP app and add CORS
app = mcp.streamable_http_app()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "DELETE", "OPTIONS"],
    allow_headers=["mcp-protocol-version", "mcp-session-id", "Content-Type"],
    expose_headers=["mcp-session-id"],
)
if __name__ == "__main__":
    uvicorn.run(app)
