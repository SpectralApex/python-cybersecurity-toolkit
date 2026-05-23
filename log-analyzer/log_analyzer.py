import re

FAILED_LOGIN_PATTERN = r'Failed password'


def analyze_log(file_path):
    failed_attempts = 0

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as log_file:
        for line in log_file:
            if re.search(FAILED_LOGIN_PATTERN, line):
                failed_attempts += 1
                print(f'[ALERT] Failed login detected: {line.strip()}')

    print(f'\nTotal Failed Login Attempts: {failed_attempts}')


if __name__ == '__main__':
    path = input('Enter log file path: ')
    analyze_log(path)
