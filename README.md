# Featured List Creator
This is a C program that generates a featured list file (`fl.cache`) from JSON data and images.

This file can then be put into your Principia user folder (as `fl.cache`) or onto a replacement web server to be downloaded by a Principia client.

## Building
You need `libjansson` and GCC. Build:

```bash
gcc main.c -ljansson -o featured-list-creator
```

## Usage
There are two optional arguments for specifying the input JSON file and output `fl.cache` file. The default values are below:

```bash
./featured-list-creator data/data.json fl.cache
```
