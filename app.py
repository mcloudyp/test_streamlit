from subprocess import Popen, PIPE, STDOUT


def exe_shell(command: str, shell: str = '/bin/bash'):
    return Popen(command, stdout=PIPE, stderr=STDOUT, shell=True, executable=shell)


if __name__ == '__main__':
    process=exe_shell(command="echo 'start to run shell script' && bash run_streamlit.sh")
    try:
        with (process.stdout):
            y = 0
            for line in iter(process.stdout.readline, b''):
                # s = str(line).replace("b'", "").replace("'", "").replace("\\n", "")
                s = line.decode('utf-8')
                print(s)
    except Exception as e:
        print(e)