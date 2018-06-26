import argparse
from time import sleep
from bs4 import BeautifulSoup
from os.path import isfile
from config import Config
from requests import get
from json import loads, dumps


def argument_parser():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--config', help='config file for health check.')
    group.add_argument('--generate', dest='generate',
                       action='store_true', help='generate example config file.')
    parser.add_argument('--force', dest='force',
                        action='store_true', help='force operation.')
    parser.add_argument('--output', dest='output', action='store',
                        choices=['json', 'txt', 'excel'], help='Special testing value')
    args = parser.parse_args()

    if args.generate == True:
        exist = isfile('./config.json')
        if exist and args.force != True:
            print('config.json file is exist. use --force argument for overwrite.')
            return
        generate_example_config()
        print('example config.json file generated.')
    elif args.config:
        config = Config(
            **loads(open(args.config, 'r', encoding='utf-8').read()))
        resps = process_config(config)
        output(config, resps)


def output(config, resps):
    if config.output == None:
        return
    file = open(f'logs.{config.output}', 'w', encoding='utf-8')
    file.write(dumps(resps, indent=4))


def process_config(config):
    resp = get(config.url)
    soup = BeautifulSoup(resp.content, 'html.parser')
    urls = soup.find_all('loc')
    if config.debug:
        print(f'{len(urls)} url will be tested.')
    resps = []
    for url in urls:
        if config.delay > 0:
            sleep(config.delay)
        resp = get(url.text)
        if config.debug:
            print(url.text, resp.status_code, resp.elapsed)
        resps.append((resp.url, resp.status_code, str(resp.elapsed)))
    return resps


def generate_example_config():
    config = Config('http://www.mysite.com/sitemap.xml')
    json = open('./config.json', 'w', encoding='utf-8')
    json.writelines(dumps(config.__dict__, indent=4, sort_keys=True))


argument_parser()
