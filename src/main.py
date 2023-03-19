import requests
import os

ABUSE_CH = 'https://mb-api.abuse.ch/api/v1/'

def ioc_update(mal_name, imphash):
    try:
        with open(mal_name + '_imphash.txt', 'a') as f:
            f.write(f'{imphash}\n')
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
        #print(res.json().get('data'))
        for x in res.json().get('data'):
            if x.get('imphash') != None:
                if x.get('imphash') != '':
                    ioc_update(tag, x.get('imphash'))

if __name__ == '__main__':
    main()