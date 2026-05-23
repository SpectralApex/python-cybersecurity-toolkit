import dns.resolver


def query_record(domain, record_type):
    try:
        answers = dns.resolver.resolve(domain, record_type)

        print(f'\n[{record_type} Records]')

        for answer in answers:
            print(answer.to_text())

    except:
        print(f'No {record_type} records found.')


if __name__ == '__main__':
    domain = input('Enter domain: ')

    for record in ['A', 'MX', 'NS', 'TXT']:
        query_record(domain, record)
