# Firecrawl MCP Documentation

## What is Firecrawl

Firecrawl is a web scraping service that crawls entire websites and converts them into clean markdown or structured data. It handles:
- Anti-bot detection
- Dynamic content loading
- Content cleaning
- Rate limiting

## Features

- **Single URL scraping**: Scrape one page and get clean markdown
- **Sitemap crawling**: Crawl all pages from a sitemap in bulk
- **LLM-ready output**: Output is clean markdown optimized for AI processing
- **Metadata extraction**: Automatically extracts title, description, links, and other metadata

## API Key

You can get an API key from:
https://firecrawl.dev/

Free tier available for testing.

## Rate Limits

- Free tier: 500 credits/month
- Paid tiers: Higher limits based on subscription

One page crawl = 1 credit.

## Best Practices

1. **Respect robots.txt**: Firecrawl respects robots.txt by default
2. **Don't scrape too fast**: Rate limiting is handled automatically
3. **Use bulk crawling for whole sites**: Use `crawl_sitemap` for entire documentation sites
4. **Extract metadata when needed**: Metadata helps with content classification

## GitHub Repository

Official MCP server: https://github.com/mendableai/firecrawl-mcp
