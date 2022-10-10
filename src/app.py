# -*- coding: utf-8 -*-
from flask import Flask, render_template
from app_modules.source_exec_module import source_exec_module

app = Flask(__name__, static_folder="view/static", template_folder="view/templates")

@app.route('/')
def index():
    return render_template("editor.html")

# ソースコード実行モジュール
app.register_blueprint(source_exec_module)


if __name__ == "__main__":
    app.run(host='0.0.0.0')