from pathlib import Path

import pandas as pd


class ToiletDataLoader:
    """トイレの開閉センサデータを読み込むクラス"""

    def read_csv(self, file_list: list[str | Path] | str | Path) -> pd.DataFrame:
        """トイレのセンサデータを読み込む
        Args:
            file_list: csvのファイルパスのリスト

        Returns:
            df: pd.DataFrame
        """
        if isinstance(file_list, str) or isinstance(file_list, Path):
            file_list = [file_list]
        output_df = []
        for file_path in file_list:
            df = pd.read_csv(
                file_path,
                usecols=[
                    "report_at",
                    "macaddress",
                    "obniz_id",
                    "is_hall_sensor_closed",
                ],
            )
            df = self._add_metadata(df)
            output_df.append(df)
        return pd.concat(output_df)

    def _add_metadata(self, df: pd.DataFrame) -> pd.DataFrame:
        """トイレのセンサデータに周辺情報を付与する"""
        df.insert(0, "timestamp", pd.to_datetime(df["report_at"]))
        df.drop(columns=["report_at"], inplace=True)
        df["macaddress"] = df["macaddress"].str.upper()
        return df


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
