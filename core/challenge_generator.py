#!/bin/python3
import logging
from tkinter import Tk  # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
import zipfile
from jinja2 import Template
import os
from utils import constants


def main():
    if not os.path.exists('logs'):
        os.makedirs('logs')

    if not os.path.exists('challenges'):
        os.makedirs('challenges')

    logging.basicConfig(filename='logs\\challenge_generator.log', level=logging.INFO, format='%(asctime)s %(message)s')
    logging.info('Started')

    challenge_name, language_choice = input().split()

    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    test_cases_zip = askopenfilename()  # show an "Open" dialog box and return the path to the selected file

    with zipfile.ZipFile(test_cases_zip, 'r') as zip_ref:
        zip_ref.extractall('challenges\\' + challenge_name + '\\data')

    generate_code_challenge(challenge_name, language_choice)

    logging.info('Finished')


def generate_code_challenge(name, language_choice):
    if language_choice not in constants.LANGUAGE:
        msg = "This language is not handled or defined"
        logging.error(msg)
        raise TypeError(msg)

    language = constants.LANGUAGE[language_choice]

    template_file = open('resources\\challenge_' + language['name'] + '_template.txt', 'r')

    tm = Template(template_file.read())

    msg = tm.render(challenge_name=name)

    code_file = open('challenges\\' + name + '\\' + name + language['extension'], 'a')
    code_file.write(msg)


if __name__ == '__main__':
    main()
