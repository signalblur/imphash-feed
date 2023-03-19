import requests
import os

ABUSE_CH = 'https://mb-api.abuse.ch/api/v1/'

def ioc_update(mal_name, imphash):
    try:
        if os.path.isfile(mal_name + '.txt'):
            os.system(f'rm {mal_name}.txt')
        with open(mal_name + '.txt', 'a') as f:
            f.write(f'{imphash}')
    except:
        pass
    
def main():
    """
    Tool to download and manage imphashes for various forms of malware.
    """

    tags = [
        'CobaltStrike',
        'N-W0rm',
        'Gh0stRAT',
        'Meterpreter',
        'Metasploit',
        'SystemBC',
        'AgentTesla',
        'njrat'
    ]

    for tag in tags:
        data = {'query':'get_taginfo', 'tag':tag, 'limit':50}
        res = requests.post(ABUSE_CH, data=data)
        ioc_update(res.json().get('data').get('signature'), res.json().get('data').get('imphash'))

if __name__ == '__main__':
    main()