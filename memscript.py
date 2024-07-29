import subprocess
import logging
import multiprocessing

logging.basicConfig(
    filename='migration_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
print("init subprocess")

def run_command(command):
    print(f"Running command: {command}")
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        
        if process.returncode != 0:
            logging.error(stderr.decode("utf-8"))
        else:
            logging.info(stdout.decode("utf-8"))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    command = "python manage.py runserver"
    p = multiprocessing.Process(target=run_command, args=(command,))
    p.start()
    p.join(5)  # Wait for 5 seconds

    if p.is_alive():
        print("Process is still running. Let's kill it.")
        p.kill()
        p.join()  # Ensure the process is cleaned up properly

    # Running other commands
    commands = [
        "python manage.py makemigrations",
        "python manage.py migrate"
    ]
    for cmd in commands:
        run_command(cmd)
