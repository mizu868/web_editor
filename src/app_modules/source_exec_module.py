from flask import Blueprint, request, jsonify
import subprocess
from datetime import datetime
import timeout_decorator

#Blueprintでモジュールの登録
source_exec_module = Blueprint('source_exec', __name__)

@source_exec_module.route("/source_exec", methods=["POST"])
def source_exec():
    print(request.form["lang"])
    lang = request.form["lang"]

    try:
        if lang == 'python':
            ret = exec_python(request.form["exec_source"])
        elif lang == 'java':
            ret = exec_java(request.form["exec_source"])

        return ret.lstrip()
        
    except Exception as e:
        return str(e)

# functions
@timeout_decorator.timeout(5, use_signals=False)
def exec_python(source):
    date_s = (datetime.now().strftime('%Y%m%d%H%M%S%f'))
    dir_path = '/opt/src/python/' + date_s
    main_file_path = dir_path + '/main.py'
    subprocess.run(['mkdir', '-p', dir_path])
    subprocess.run(['touch', main_file_path])
    with open(main_file_path, 'w') as f:
        f.write(source)

    ret = subprocess.run(['python3', 'main.py'], capture_output=True, encoding='utf8', cwd=dir_path)
    if len(ret.stdout) != 0:
        ret_str = ret.stdout
    else:
        ret_str = ret.stderr
    subprocess.run(['rm', '-rf', dir_path])

    return ret_str

@timeout_decorator.timeout(5, use_signals=False)
def exec_java(source):
    date_s = (datetime.now().strftime('%Y%m%d%H%M%S%f'))
    dir_path = '/opt/src/java/' + date_s
    main_file_path = dir_path + '/Main.java'
    subprocess.run(['mkdir', '-p', dir_path])

    with open(main_file_path, "w") as f:
        f.write(source)

    java_compile = subprocess.run(['javac', '-encoding', 'UTF-8', main_file_path], capture_output=True, encoding='utf8')
    if len(java_compile.stderr) != 0:
        subprocess.run(['rm', '-rf', dir_path])
        return java_compile.stderr
    else:
        java_exec = subprocess.run(['java', '-Dfile.encoding=UTF-8', 'Main'], capture_output=True, encoding='utf8', cwd=dir_path)
        if len(java_exec.stderr) != 0:
            subprocess.run(['rm', '-rf', dir_path])
            return java_exec.stderr
        else:
            subprocess.run(['rm', '-rf', dir_path])
            return java_exec.stdout