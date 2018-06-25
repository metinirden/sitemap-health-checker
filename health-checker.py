import argparse
from os.path import isfile
from config import Config
from json import loads, dumps


def argument_parser():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--config', help='config file for health check.')
    group.add_argument('--generate', dest='generate',
                       action='store_true', help='generate example config file.')
    parser.add_argument('--force', dest='force', action='store_true', help='')
    args = parser.parse_args()

    if args.generate == True:
        exist = isfile('./config.json')
        if exist and args.force != True:
            print('config.json file is exist. use --force argument for overwrite.')
            return
        generate_example_config()
        print('example config.json file generated.')
    elif args.config:
        config = Config(**loads(open(args.config, 'r').read()))
        print(config)


def generate_example_config():
    config = Config('http://www.mysite.com/sitemap.xml')
    json = open('config.json', 'w', encoding='utf-8')
    json.writelines(dumps(config.__dict__, indent=4, sort_keys=True))


argument_parser()
