#!/usr/bin/env python3
# Purpose: Fetch the webpage and save it to a file

import requests, argparse, re

def get_args():
    '''
    Getting command line arguments
    '''
    
    parser = argparse.ArgumentParser(description='Fetch web pages', formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('links', nargs='*', help='Links to be fetched and saved', metavar='URLs', type=str)         # For getting link arguments

    parser.add_argument('-m', '--metadata', nargs=1, help='Show the metadata information for a link', metavar='str', type=str)           # For getting metadata arguments

    return parser.parse_args()

def main():
    '''
    Downloading and saving the metadata
    '''
    args = get_args()

    urls = args.links
    meta = args.metadata

    if urls == [] and not meta:
        print('No URLs provided')
        return

    for item in urls:
        try:
            r = requests.get(item)
            url_pattern = re.search('https?://([A-Za-z_0-9.-]+).*', item)                               # To store the base domain of the URL
            basedomain = url_pattern.group(1)
            response = r.text.lower()

            if '<!doctype html>' in response:                                                           # To check if the response is in HTML format
                with open(f'{basedomain}.html', 'w') as f:
                    f.write(r.text)
            else:
                raise Exception(f'Response for URL: "{item}" is in a different format than HTML')       # Exception handling for any format other than HTML
        except Exception as e:                                                                          # Exception handling for any other errors
            print(e)



if __name__ == '__main__':
    main()
