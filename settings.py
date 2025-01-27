import os
import json

IS_DOCKER = os.environ.get('IS_DOCKER', '')

# Load config
settingsf = open('settings.json')
settings = json.load(settingsf)

TOKEN = settings['DEFAULT']['TOKEN']
PREFIX = [x for x in settings['DEFAULT']['PREFIX']]
STATUS = settings['DEFAULT']['STATUS']
staff_roles = [x for x in settings['MODERATOR']]
