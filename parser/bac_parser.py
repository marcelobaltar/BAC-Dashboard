import logging

def main():
	logging.basicConfig(level=logging.INFO)
	logging.warning('Watch out!')
	logging.info('I told you so')

if __name__ == '__main__':
	main()
