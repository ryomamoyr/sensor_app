# src/app.py

import streamlit as st
from dataloader.toilet import ToiletDataLoader
from analyser.toilet import ToiletAnalyser
from visualizer.toilet import ToiletVisualizer

# ページの設定
st.set_page_config(
    page_title="トイレセンサデータ分析アプリ",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("トイレセンサデータ分析アプリ")

# サイドバーにファイルアップロード
# st.sidebar.header("CSVファイルのアップロード")
uploaded_files = st.sidebar.file_uploader(
    "CSVファイルをアップロードしてください", type="csv", accept_multiple_files=True
)


# データのロードと処理をキャッシュ
@st.cache_data
def load_and_process(uploaded_files):
    """
    データのロードと処理を行う関数
    Returns:
        data: ロードしたデータ
        result_df: 日次利用状況の要約
        imos_df: IMOSのデータ
        visualizer: 可視化オブジェクト
    """
    loader = ToiletDataLoader()
    data = loader.read_csv(uploaded_files)

    analyser = ToiletAnalyser(data)
    result_df = analyser.summarize_daily_usage()
    imos_df = analyser.make_imos_df(result_df)

    visualizer = ToiletVisualizer(result_df)

    return data, result_df, imos_df, visualizer


# 可視化部分を関数化
def display_charts(visualizer, imos_df):
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("時間帯ごとのトイレ利用台数")
        fig_time = visualizer.plot_usage_over_time(imos_df)
        st.plotly_chart(fig_time, use_container_width=True)

    with col2:
        st.subheader("個室ごとの利用回数")
        fig_stall = visualizer.plot_usage_count_by_stall()
        st.plotly_chart(fig_stall, use_container_width=True)


if uploaded_files:
    try:
        # データのロードと処理
        data, result_df, imos_df, visualizer = load_and_process(uploaded_files)
    except Exception as e:
        st.error(f"データの処理中にエラーが発生しました: {e}")
        st.stop()

    # アップロードされたデータのプレビュー
    st.subheader("アップロードされたデータのプレビュー")
    st.dataframe(data.head())

    # 分析結果の表示
    st.subheader("日次利用状況の要約")
    st.dataframe(result_df)

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
