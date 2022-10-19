#!/usr/bin/env python3
# Purpose: Fetch the webpage and save it to a file

import requests, argparse

def get_args():
    '''
    Getting command line arguments
    '''
    
    parser = argparse.ArgumentParser(description='Fetch web pages', formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('links', nargs='+', help='Links to be fetched and saved', metavar='URLs', type=str)

    # parser.add_argument('--metadata', nargs='+', help='Links to be fetched and saved', metavar='str', type=str)

    return parser.parse_args()

def main():
    args = get_args()

    urls = args.links

    print(urls)

if __name__ == '__main__':
    main()