import pandas as pd
import plotly.express as px


class ToiletVisualizer:
    def __init__(self, result_df: pd.DataFrame):
        self.result_df = result_df

    def plot_usage_over_time(self, imos_df: pd.DataFrame):
        """時間帯ごとのトイレ利用台数をプロット"""
        fig = px.line(
            imos_df.reset_index(),
            x="index",
            y="usage_count",
            title="時間帯ごとのトイレ利用台数",
            labels={"index": "時間", "usage_count": "利用台数"},
            template="plotly_dark",
        )
        fig.update_layout(
            xaxis_tickformat="%H:%M", font=dict(size=14), title_font_size=24
        )
        return fig

    def plot_usage_count_by_stall(self):
        """個室ごとの利用回数をプロット"""
        # 個室ごとの利用回数を集計
        usage_counts = (
            self.result_df.groupby("macaddress").size().reset_index(name="usage_count")
        )

        # プロットを作成
        fig = px.bar(
            usage_counts,
            x="macaddress",
            y="usage_count",
            title="個室ごとの利用回数",
            labels={"macaddress": "個室（MACアドレス）", "usage_count": "利用回数"},
            template="plotly_dark",
        )
        fig.update_layout(
            xaxis_tickangle=-45,  # X軸のラベルを見やすくするために傾ける
            font=dict(size=14),
            title_font_size=24,
        )
        return fig
