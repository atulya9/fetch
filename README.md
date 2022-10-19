# Fetch
This is a simple CLI written in Python which downloads HTML pages from provided links

## How to use this CLI
This CLI takes the following arguments:
1. URL (positional): It takes any number of URLs as positional arguments and it will download all the pages and save them in an HTML format.
2. Metadata (-m, --metadata): It saves the following metadata in a JSON file: site name, number of images in the page, number of links in the page and the time when the page was last updated.

## Example
1. The below example will download the Google and Facebook homepage and save them in an HTML format with filenames 'www.google.com.html' and 'www.facebook.com.html' respectively
```
./fetch.py https://www.google.com https://www.facebook.com
```

Output:
```
HTML saved for site: www.google.com at ./www.google.com.html
HTML saved for site: www.facebook.com at ./www.facebook.com.html
```

2. The below example will print the metadata as mentioned above
```
./fetch.py -m www.google.com
```

Output:
```
site: www.google.com
num_links: 27
images: 1
last_fetch: some date
```

Note: To run it without using `python` or `python3` the command `chmod +x fetch.py` needs to be executed to make the file executable.

## Running in a docker container
This CLI can also be run using docker using the Dockerfile provided. To run it using docker run the following commands
1. To build the docker image
```
docker build -t image-name .
```

2. To run the image
```
docker run image-name <URLs> --metadata <URL>
```