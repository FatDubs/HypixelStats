# dubs#9025
# Hypixel Stats
# 1/31/21

import yaml
from bot import Thread
##TODO: add logging
#import logging

def main():
    config = yaml.safe_load(open('config.yml'))
    bot = bot.Thread(config['email'],config['password'],config['rate'],config['admins'])
    bot.start()


if __name__ == "__main__":
    main()