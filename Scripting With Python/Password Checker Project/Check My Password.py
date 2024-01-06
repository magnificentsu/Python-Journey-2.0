import requests
import hashlib
import sys

def request_api_data(query_characters):
    url = 'https://api.pwnedpasswords.com/range/' + query_characters
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f'Error fetiching: {response.status_code}, check API and try again')
    return response
    # print(res)

def read_response(response1):
    print(response1.text)

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0
def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_characters = sha1password[:5]
    tail = sha1password[5:]
    response2 = request_api_data(first5_characters)
    print(first5_characters, tail)
    print(response2)
    return get_password_leaks_count(response2, tail)

def main(args):
    for passwords in args:
        count = pwned_api_check(passwords)
        if count:
            print(f'{passwords} was found {count} time.  You should probably change your password')
        else:
            print(f'{passwords} was NOT found. Carry on!')
    return 'DONE!'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
