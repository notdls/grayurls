import requests
import argparse
import os
import logging
import sys

def get_urls(target, api_key):
    s = requests.Session()
    s.headers.update({"User-Agent":"grayurls (https://github.com/notdls/grayurls)"})
    # get initial resp
    response = s.get("https://shorteners.grayhatwarfare.com/api/v1/subdomain/{}/files/0/1?access_token={}".format(target, api_key)).json()
    url_count = response["urlsCount"]
    logging.debug("{} available for {}, {} requests are required, grabbing now".format(url_count, target, int(url_count/1000)+1))
    # scrape all the urls and print to stdout
    for i in range(0, url_count, 1000):
        try:
            batch = s.get("https://shorteners.grayhatwarfare.com/api/v1/subdomain/{}/files/{}/1000?access_token={}".format(target, i, api_key)).json()
            #print(batch)
            if "urls" in batch:
                for url in batch["urls"]:
                    print(url["url"])
            elif "error" in batch:
                if "Results listing is limited to protect resources." in batch["error"]:
                    logging.debug("Scraping stopped due to API limitations, to get around this you will need to upgrade your account")
                    break
                else:
                    logging.debug("Unknown response received from server: {}".format(batch["error"]))
            else:
                logging.debug("No url in batch?")
        except Exception as e:
            logging.debug(str(e))

def main():
    # Parse Arguments
    parser = argparse.ArgumentParser(description="Grabs shortned URLs for a given site from the GrayHatWarfare Shorteners API")
    parser.add_argument('-t','--target', type=str, action="store", dest="target", help="Target domain/subdomains (e.g. example.com)", required=True)
    parser.add_argument('-d','--debug', type=bool, action="store", dest="debug", help="Print debug information", default=False)
    args = parser.parse_args()

    # Setup logging
    if args.debug:
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        root.addHandler(handler)

    # Check if API key is setup, env var called GRAYHATWARFARE_API_KEY
    if os.getenv("GRAYHATWARFARE_API_KEY"):
        api_key = os.getenv("GRAYHATWARFARE_API_KEY")
    else:
        print("An API key is required to use this script, please register to obtain one at https://grayhatwarfare.com/register. If you already have one, please set your API key using environment variables, e.g. export GRAYHATWARFARE_API_KEY=key")
        exit()

    # setup debug logging if requested
    if args.debug:
        logging.basicConfig(filename='debug.log', level=logging.DEBUG)
        logging.debug("Debug level set")
    
    # do the thing
    get_urls(args.target, api_key)

if __name__ == "__main__":
    main()
