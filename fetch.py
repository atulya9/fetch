#!/usr/bin/env python3
# Purpose: Fetch the webpage and save it to a file

from sys import meta_path
import requests
import argparse
import re
import json
from bs4 import BeautifulSoup       # For counting the number of links and images


def get_args():
    '''
    Getting command line arguments
    '''
    
    parser = argparse.ArgumentParser(description='Fetch web pages', formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('links', nargs='*', help='Links to be fetched and saved', metavar='URLs', type=str)         # For getting link arguments

    parser.add_argument('-m', '--metadata', help='Show the metadata information for a link. Takes the base domain as argument', metavar='str', type=str)           # For getting metadata arguments

    return parser.parse_args()

def main():
    '''
    Downloading and saving the metadata
    '''
    args = get_args()

    urls = args.links
    meta_id = args.metadata

    try:                                                                                                # Checking if the metadata file exists or not
        meta_data = json.load(open('metadata.json'))
    except FileNotFoundError:
        meta_data = {}

    if urls == [] and not meta_id:                                                                      # Handling empty arguments
        print('No URLs provided and no metadata requested')
        return

    for item in urls:
        try:
            r = requests.get(item)

            url_pattern = re.search('https?://([A-Za-z_0-9.-]+).*', item)                               # To store the base domain of the URL
            basedomain = url_pattern.group(1)

            soup = BeautifulSoup(r.content, features="html.parser")
            img_count = len(soup.find_all('img'))
            link_count = len(soup.find_all('a'))
            last_fetch = r.headers['Date']

            new_entry = {'num_links': link_count, 'images':img_count, 'last_fetch': last_fetch}

            if 'html' in r.headers['Content-Type']:                                                           # To check if the response is in HTML format
                with open(f'{basedomain}.html', 'w') as f:
                    f.write(r.text)
                    meta_data[basedomain] = new_entry
                    print(f'HTML saved for site: {basedomain} at ./{basedomain}.html')
            else:
                raise Exception(f'Response for URL: "{item}" is in a different format than HTML')       # Exception handling for any format other than HTML
        except Exception as e:                                                                          # Exception handling for any other errors
            print(e)

    json.dump(meta_data, open('metadata.json', 'w'))                                                    # Updating the JSON file

    if meta_id:
        try:
            meta_data = json.load(open('metadata.json'))
            vals = meta_data[meta_id]
            print(f'site: {meta_id}')
            for item in vals:
                print(f'{item}: {vals[item]}')
        except Exception as e:
            print('e')


if __name__ == '__main__':
    main()
