import pandas as pd
import streamlit as st
from dataloader.toilet import ToiletDataLoader
from analyser.toilet import ToiletAnalyser
from visualizer.toilet import ToiletVisualizer

# ページの設定
st.set_page_config(
    page_title="Sensor Data Analysis App",
    layout="wide",
    initial_sidebar_state="expanded",
)

# センターレイアウト
st.title("トイレセンサデータ分析アプリ")

# サイドバーにファイルアップロード
st.sidebar.title("Menu")
menu_option = st.sidebar.selectbox(
    "Select Analysis Data", ["Toilet", "Trash can", "Other"]
)

# アップロードされたファイルを格納する変数
uploaded_files = None

# 選択したメニューに応じたコンテンツを表示
if menu_option == "Toilet":
    uploaded_files = st.sidebar.file_uploader(
        "Toilet: CSVファイルをアップロードしてください",
        type="csv",
        accept_multiple_files=True,
    )
elif menu_option == "Trash can":
    uploaded_files = st.sidebar.file_uploader(
        "Trash can: CSVファイルをアップロードしてください",
        type="csv",
        accept_multiple_files=True,
    )
elif menu_option == "Other":
    uploaded_files = st.sidebar.file_uploader(
        "Other: CSVファイルをアップロードしてください",
        type="csv",
        accept_multiple_files=True,
    )


# データのロードと処理をキャッシュ
@st.cache_data
def load_and_process(uploaded_files):
    """
    データのロードと処理を行う関数
    Returns:
        data (pd.DataFrame): ロードしたデータ
        result_df (pd.DataFrame): 日次利用状況の要約
        imos_df (pd.DataFrame): IMOSのデータ
        visualizer (ToiletVisualizer): 可視化オブジェクト
    """
    data_frames = []
    for uploaded_file in uploaded_files:
        try:
            df = pd.read_csv(uploaded_file)
            data_frames.append(df)
        except Exception as e:
            st.error(f"ファイルの読み込み中にエラーが発生しました: {e}")
            st.stop()

    loader = ToiletDataLoader()
    try:
        data = loader.read_csv(data_frames)
    except Exception as e:
        st.error(f"ToiletDataLoaderでエラーが発生しました: {e}")
        st.stop()

    try:
        analyser = ToiletAnalyser(data)
        result_df, imos_df = analyser.summarize_daily_usage()
    except Exception as e:
        st.error(f"ToiletAnalyserでエラーが発生しました: {e}")
        st.stop()

    try:
        visualizer = ToiletVisualizer(result_df)
    except Exception as e:
        st.error(f"ToiletVisualizerの初期化中にエラーが発生しました: {e}")
        st.stop()

    return data, result_df, imos_df, visualizer


# 可視化部分を関数化
def display_charts(visualizer, imos_df):
    col1, col2 = st.columns(2)

    with col1:
        fig_time = visualizer.plot_usage_over_time(imos_df)
        if fig_time:
            st.plotly_chart(fig_time, use_container_width=True)

    with col2:
        fig_stall = visualizer.plot_usage_count_by_stall()
        if fig_stall:
            st.plotly_chart(fig_stall, use_container_width=True)


if uploaded_files:
    try:
        # データのロードと処理
        data, result_df, imos_df, visualizer = load_and_process(uploaded_files)
    except Exception as e:
        st.error(f"データの処理中にエラーが発生しました: {e}")
        st.stop()

    # アップロードされたデータのプレビュー
    st.subheader("data preview")
    st.dataframe(data.head())

    # 可視化
    display_charts(visualizer, imos_df)

    # ダウンロードリンクの提供
    st.subheader("分析結果のダウンロード")
    csv = result_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="CSVとしてダウンロード",
        data=csv,
        file_name="daily_usage_summary.csv",
        mime="text/csv",
    )
else:
    st.info("サイドバーからCSVファイルをアップロードしてください。")

st.markdown(
    """
---
<div style="text-align: center; color: #888888;">
    &copy; 2024 ry | <a href="mailto:your.email@example.com">your.email@example.com</a>
</div>
""",
    unsafe_allow_html=True,
)
