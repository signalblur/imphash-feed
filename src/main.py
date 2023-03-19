import os
import time
import subprocess
import requests

ABUSE_CH = 'https://mb-api.abuse.ch/api/v1/'

def ioc_update(mal_name, imphash):
    file_path = mal_name + '_imphash.txt'
    
    if os.path.exists(file_path):
        file_path = mal_name + '_imphash.txt'
        with open(file_path, 'r+') as f:
            file_content = f.read()
            if imphash not in file_content:
                f.write(f'{imphash}\n')
    else:
        with open(file_path, 'a') as f:
            f.write(f'{imphash}\n')

def main():
    """
    Tool to download and manage imphashes for various forms of malware.
    """
    while True:
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
            holder = []
            data = {'query':'get_taginfo', 'tag':tag, 'limit':50}
            res = requests.post(ABUSE_CH, data=data)
            #print(res.json().get('data'))
            for x in res.json().get('data'):
                if x.get('imphash') != None:
                        if x.get('imphash') not in holder:
                            ioc_update(tag, x.get('imphash'))
                            holder.append(x.get('imphash'))
        subprocess.run(['git', 'add', '*', '&&', 'git', 'commit', '-m', '"updates"', '&&', 'git', 'push'])
        time.sleep(15*60)

if __name__ == '__main__':
    main()