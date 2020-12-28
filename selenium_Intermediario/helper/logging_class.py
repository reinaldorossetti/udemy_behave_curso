import logging
from os import path, getcwd

class Logger(object):

    def __init__(self, name="mylog.log"):
        # pega o caminho do projeto.
        path_app = getcwd()
        # remove o .log que jah eh gerado pela funcao.
        name = name.replace('.log','')
        # log_namespace can be replaced with your namespace - 'log_namespace.%s' % name
        logger = logging.getLogger(name)
        # Defina o nível de log. Nível deve ser um int ou um str.
        logger.setLevel(logging.DEBUG)
        if not logger.handlers:
            file_name = path.join(path_app, 'logs','%s.log' % name)
            print(file_name)
            handler = logging.FileHandler(file_name)
            # Define uma formatacao para o log adicionando a data no formato  %d/%m/%Y %I:%M:%S %p.
            # Voce pode remover a data e o Nivel e deixar somente a %(message)s
            formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s',
             datefmt='%d/%m/%Y %I:%M:%S %p')
            handler.setFormatter(formatter)
            handler.setLevel(logging.DEBUG)
            logger.addHandler(handler)
        self._logger = logger

    def get(self):
        return self._logger
