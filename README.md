## grayurls
------

A common workflow when performing reconnaissance on a target domain or web application is identifying potential paths or content, this is commonly performed by retrieving indexed URLs from services such as archive.org and Common Crawl using tools like [waybackurls](https://github.com/tomnomnom/waybackurls) and [gau](https://github.com/lc/gau). This tool is inspired by them and very similar, retrieving URLs that have once been shortened by a URL shortening service (e.g. goo.gl, bit.ly, etc.) using [GrayhatWarfare's API](https://shorteners.grayhatwarfare.com/docs/api/v1). They currently have a database of ~1.1 billion resolved short URLs, which may contain sensitive or otherwise interesting paths or endpoints. 

## Limitations
To utilise this tool you will need to have a valid API key for the GrayhatWarfare API, [registration](https://grayhatwarfare.com/register) is free and will provide you access to the first ~5,000 results for any given domain/subdomain. However, any records beyond the 4,000 mark will require a premium subscription.

## Usage & Examples
Setting API key environment variable
```
export GRAYHATWARFARE_API_KEY=key
```
Examples
```
$ grayurls --target google.com
$ grayurls -t google.com
```
Usage
```
usage: grayurls.py [-h] -t TARGET [-d DEBUG]

Scraped shortned URLs for a given site from the GrayHatWarefare Shorteners API

optional arguments:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        Target domain/subdomains (e.g. example.com)
  -d DEBUG, --debug DEBUG
                        Print debug information
```

## Contributing 
Issues, contributions, pull requests, etc, all welcome.