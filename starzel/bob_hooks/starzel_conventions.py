def starzel_conventions(configurator, question, answer):
    if answer.lower() in ['t', 'y', 'j', 'true', 'yes', 'ja', '1']:
        for question in configurator.questions:
            if question.name == 'local.backupdir':
                question.default = '/home/starzel/backup/${buildout:site}'
            if question.name == 'local.vardir':
                question.default = '/home/starzel/var/${buildout:site}'
    return answer
