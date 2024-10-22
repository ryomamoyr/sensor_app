# backend/dataloader/toilet.py

from pathlib import Path
import pandas as pd


class ToiletDataLoader:
    """トイレの開閉センサデータを読み込むクラス"""

    def read_csv(self, data_frames: list[pd.DataFrame]) -> pd.DataFrame:
        """トイレのセンサデータを結合する
        Args:
            data_frames: 読み込まれたデータフレームのリスト

        Returns:
            pd.DataFrame: 結合されたデータフレーム
        """
        if not data_frames:
            raise ValueError("No data frames to load.")
        combined_data = pd.concat(data_frames, ignore_index=True)
        combined_data = self._add_metadata(combined_data)
        return combined_data

    def _add_metadata(self, df: pd.DataFrame) -> pd.DataFrame:
        """トイレのセンサデータに周辺情報を付与する"""
        df.insert(0, "timestamp", pd.to_datetime(df["report_at"]))
        df.drop(columns=["report_at"], inplace=True)
        df["macaddress"] = df["macaddress"].str.upper()
        return df


# NOTE: これはエスコン専用のコードで、上をBaseclassにして下を付与したい
#         """トイレのセンサデータに周辺情報を付与する"""
#         df.insert(0, "timestamp", pd.to_datetime(df["report_at"]))
#         df.drop(columns=["report_at"], inplace=True)
#         df["macaddress"] = df["macaddress"].str.upper()
#         # macaddressから個室名を取得
#         df["room"] = df["macaddress"].map(
#             lambda x: self.cfg.master.toilet[x]["name"]
#             if x in self.cfg.master.toilet.keys()
#             else None
#         )
#         df.dropna(subset=["room"], inplace=True)
#         # 個室名から階数とエリア名を取得
#         df["floor"] = df["room"].map(lambda x: x.split("_")[0])
#         df["area"] = (
#             df["room"].map(lambda x: x.split("_")[0])
#             + "_"
#             + df["room"].map(lambda x: x.split("_")[1])
#         )
#         return df
#
