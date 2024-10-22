# run_main.py

import streamlit.web.cli as stcli
import os
import sys


def streamlit_run():
    # 実行ファイルのディレクトリを取得
    base_path = os.path.dirname(os.path.abspath(__file__))
    # `src/app.py`へのパスを構築
    src = os.path.join(base_path, "src", "app.py")
    sys.argv = ["streamlit", "run", src, "--global.developmentMode=false"]
    sys.exit(stcli.main())


if __name__ == "__main__":
    streamlit_run()
