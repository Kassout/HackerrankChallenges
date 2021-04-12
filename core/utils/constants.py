# Declare constants in a separate file called constant.py
LANGUAGE = {
    '0': {'name': 'python', 'extension': '.py'},
    '1': {'name': 'csharp', 'extension': '.cs'}
}

SKILL = {
    '0': {'name': 'interview preparation kit', 'path_name': 'InterviewPreparationKit',
          'compatibility': [language for language in LANGUAGE.values()]},
    '1': {'name': 'python', 'path_name': 'Python',
          'compatibility': [LANGUAGE['0']]},
    '2': {'name': 'algorithms', 'path_name': 'Algorithms',
          'compatibility': [language for language in LANGUAGE.values()]},
    '3': {'name': 'data structures', 'path_name': 'DataStructures',
          'compatibility': [language for language in LANGUAGE.values()]}
}