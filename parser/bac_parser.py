import logging
import logging.config

# Configura o logger
# Level of logging: DEBUG -> INFO -> WARNING (default) -> ERROR -> CRITICAL
logging.config.fileConfig('log.config')
logger = logging.getLogger('parser')

def main():
	logger.warning('Watch out!')
	logger.info('I told you so')
	logger.debug('Teste')

if __name__ == '__main__':
	main()
