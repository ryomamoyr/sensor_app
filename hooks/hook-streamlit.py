from PyInstaller.utils.hooks import copy_metadata

# Streamlitのメタデータを含める
datas = copy_metadata("streamlit")

