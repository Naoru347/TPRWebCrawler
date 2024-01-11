import subprocess

def run_script(script_name):
    try:
        subprocess.run(["python", script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running {script_name}: {e}")

def main():
    run_script("TPRArticleSaver.py")
    run_script("TPRHTMLSaver.py")

if __name__ == "__main__":
    main()
