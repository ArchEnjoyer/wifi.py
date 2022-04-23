import  subprocess


def extract_wifi_passwords(codec):
    
    profiles_data = subprocess.check_output('netsh wlan show profiles').decode(codec).split('\n')
    profiles = [i.split(':')[1].strip() for i in profiles_data if ':' in i]
    
    for ty in range(1, len(profiles)):
        profile = profiles[ty]
        profile_info = subprocess.check_output(f'netsh wlan show profile {profile} key=clear').decode(codec)

        with open(file='wifi_passwords.txt', mode='a', encoding='utf-8') as file:
            file.write(f'Profile: {profile}\nInfo: {profile_info}\n{"#" * 100}\n')
        

def main():
    codecs = ["cp1252", "cp437", "utf-16be", "utf-16", "utf-8", "ansi", "cp1251", "ascii", "cp866"]
    for codec in codecs:
        try: extract_wifi_passwords(codec)
        except BaseException: continue

if __name__ == '__main__':
    main()
