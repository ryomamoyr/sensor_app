import streamlit as st
from dataloader.toilet import ToiletDataLoader
from analyser.toilet import ToiletAnalyser
from visualizer.toilet import ToiletVisualizer

# ページ設定
st.set_page_config(
    page_title="トイレセンサデータ分析アプリ",
    page_icon="🚽",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("トイレセンサデータ分析アプリ")

# ファイルアップロード
uploaded_files = st.file_uploader(
    "CSVファイルをアップロードしてください", type="csv", accept_multiple_files=True
)
if uploaded_files:
    try:
        # データのロード
        loader = ToiletDataLoader()
        data = loader.read_csv(uploaded_files)
        # データの分析
        analyser = ToiletAnalyser(data)
        result_df = analyser.summarize_daily_usage()
        # Imos法による時間帯ごとの利用台数の計算
        imos_df = analyser.make_imos_df(result_df)
        # データの可視化
        visualizer = ToiletVisualizer(result_df)

        # カラムを作成して図を横に配置
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("時間帯ごとのトイレ利用台数")
            fig_time = visualizer.plot_usage_over_time(imos_df)
            st.plotly_chart(fig_time, use_container_width=True)

        with col2:
            st.subheader("個室ごとの利用回数")
            fig_stall = visualizer.plot_usage_count_by_stall()
            st.plotly_chart(fig_stall, use_container_width=True)
    except Exception as e:
        st.error(f"エラーが発生しました: {e}")
else:
    st.info("左側のパネルからCSVファイルをアップロードしてください。")
