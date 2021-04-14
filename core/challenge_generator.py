#!/bin/python3
import os
import logging
import zipfile
from jinja2 import Template
from utils import constants
from tkinter import Tk  # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename


def main():
    instantiate_logs()
    logging.info('Started')

    if not os.path.exists('challenges'):
        logging.info('No <challenges> folder, generation...')
        os.makedirs('challenges')
        logging.info('<challenges> folder generation done.')

    challenge_name = input("Hello! Want to work on a new challenge?\nPlease give it a name: ")

    skill_choice = choose_challenge_category()
    language_choice = choose_challenge_language(skill_choice)

    challenge_path = generate_folder_and_starter_files(challenge_name, skill_choice, language_choice)

    generate_code_challenge(challenge_name, challenge_path, language_choice)
    generate_test_challenge(challenge_name, challenge_path, language_choice)
    generate_run_challenge(challenge_name, challenge_path, language_choice)

    logging.info('Ended')


def instantiate_logs():
    if not os.path.exists('logs'):
        os.makedirs('logs')

    logging.basicConfig(filename='logs\\challenge_generator.log', level=logging.INFO, format='%(asctime)s %(message)s')


def choose_challenge_category():
    logging.info('Start challenge category choice.')
    skill_choice = None

    while skill_choice not in list(constants.SKILL.keys()):
        print("Please choose a challenge category:")
        for i, skill in enumerate(constants.SKILL.values()):
            print(str(i) + ") " + skill['name'])
        skill_choice = input("Answer: ")
    skill_choice = constants.SKILL[skill_choice]

    logging.info('End challenge category choice.')
    return skill_choice


def choose_challenge_language(skill_choice):
    logging.info('Start challenge language choice.')
    language_choice = None

    logging.info('End challenge category choice.')
    if len(skill_choice['compatibility']) > 1:
        while language_choice not in list(constants.LANGUAGE.keys()):
            print("Please choose a compatible language:")
            for i, language in enumerate(skill_choice['compatibility']):
                print(str(i) + ") " + language['name'])
            language_choice = input("Answer: ")
        language_choice = constants.LANGUAGE[language_choice]
    else:
        language_choice = skill_choice['compatibility'][0]

    logging.info('End challenge language choice.')
    return language_choice


def generate_folder_and_starter_files(challenge_name, skill_choice, language_choice):
    logging.info('Start folder and starter files generation.')
    challenge_path = 'challenges\\' + skill_choice['path_name'] + '\\' + challenge_name + \
                     (('\\' + language_choice['name'] + '\\') if len(skill_choice['compatibility']) > 1 else '\\')
    os.makedirs(challenge_path)

    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    test_cases_zip = askopenfilename()  # show an "Open" dialog box and return the path to the selected file

    with zipfile.ZipFile(test_cases_zip, 'r') as zip_ref:
        zip_ref.extractall(challenge_path + 'data')

    logging.info('End folder and starter files generation.')
    return challenge_path


def generate_code_challenge(name, path, language_choice):
    logging.info('Start challenge code generation.')
    template_file = open('resources\\challenge_' + language_choice['name'] + '_template.txt', 'r')

    tm = Template(template_file.read())
    msg = tm.render(challenge_name=name)

    code_file = open(path + name + language_choice['extension'], 'a')
    code_file.write(msg)
    logging.info('End challenge code generation.')


def generate_test_challenge(name, path, language_choice):
    logging.info('Start challenge tests code generation.')
    os.makedirs(path + 'tests')
    template_file = open('resources\\test_challenge_' + language_choice['name'] + '_template.txt', 'r')

    outputs = []
    for filename in os.listdir(path + 'data\\output'):
        if filename.endswith(".txt"):
            outputs.append(''.join(c for c in filename if c.isdigit()))

    tm = Template(template_file.read())
    msg = tm.render(challenge_name=name, class_test_name=''.join(x.capitalize() for x in name.split('_')), outputs=outputs)

    code_file = open(path + 'tests\\test_' + name + language_choice['extension'], 'a')
    code_file.write(msg)
    logging.info('End challenge tests code generation.')


def generate_run_challenge(name, path, language_choice):
    logging.info('Start run challenge bash script generation.')
    template_file = open('resources\\run_' + language_choice['name'] + '_challenge_shell_template.txt', 'r')

    tm = Template(template_file.read())
    msg = tm.render(challenge_name=name)

    code_file = open(path + 'run_challenge.sh', 'a')
    code_file.write(msg)
    logging.info('End run challenge bash script generation.')


if __name__ == '__main__':
    main()
