from pathlib import Path

import numpy as np
import pandas as pd


class ToFDataLoader:
    """ToFセンサのデータを読み込む基底クラス"""

    def read_csv(self, data_frames: list[pd.DataFrame]) -> pd.DataFrame:
        """ToFセンサデータを読み込む
        Args:
            path_list: list[str | Path] | str | Path : csvのファイルパスのリスト
        Returns:
            df: pd.DataFrame
        """
        if not data_frames:
            raise ValueError("No data frames to load.")
        for file_path in file_list:
            df = self._load(file_path)
            output_df.append(df)
        output_df = pd.concat(output_df)
        return output_df

    def _load(self, file_path: Path | str) -> pd.DataFrame:
        """ゴミ箱のToFセンサデータを読み込み、マスタデータを基に周辺情報を付与する
        Args:
            path: str

        Returns:
            df: pd.DataFrame
        """
        df = pd.read_csv(file_path, usecols=["logged_at", "macaddress", "distance"])
        df.insert(0, "timestamp", pd.to_datetime(df["logged_at"]))
        df.drop(columns=["logged_at"], inplace=True)
        df["macaddress"] = df["macaddress"].str.upper()
        df["box_name"] = df["macaddress"].map(
            lambda x: self.config.master.tof.get(x, {}).get("name")
        )
        df.dropna(subset=["box_name"], inplace=True)
        df["kind"] = df["box_name"].map(lambda x: x.split("_")[0].split("-")[-1])
        df["box_area"] = df["box_name"].map(lambda x: x.split("-")[0])
        dfs = []
        for mac in df["macaddress"].unique():
            tmp = df[df["macaddress"] == mac]
            tmp = self._add_capacity(tmp)
            dfs.append(tmp)
        df = pd.concat(dfs)
        df["x"] = df["macaddress"].map(
            lambda i: self.config.master.tof.get(i, {}).get("x", np.nan),
            na_action="ignore",
        )
        df["y"] = df["macaddress"].map(
            lambda i: self.config.master.tof.get(i, {}).get("y", np.nan),
            na_action="ignore",
        )
        df["floor"] = df["macaddress"].map(
            lambda i: self.config.master.tof.get(i, {}).get("floor", np.nan),
            na_action="ignore",
        )
        df.reset_index(inplace=True, drop=True)
        return df

    def _add_capacity(self, input_df: pd.DataFrame) -> pd.DataFrame:
        """ToFセンサの距離情報をもとにゴミ箱の容量を計算する
        Args:
            input_df: pd.DataFrame
        Returns:
            df: pd.DataFrame
        """
        df = input_df.copy()
        df.sort_values(["timestamp"], inplace=True)
        # 外れ値処理(1分で100mm以上移動した場合は外れ値として線形補間する)
        df["diff"] = df["distance"].diff()
        df["diff"] = df["diff"].fillna(0)
        df["diff"] = df["diff"].abs()
        df["distance"] = df.apply(
            lambda x: x["distance"] if x["diff"] < 100 else np.nan, axis=1
        )
        df["distance"].interpolate(method="linear", inplace=True)
        df.drop(columns=["diff"], inplace=True)
        df.reset_index(inplace=True, drop=True)
        drink_level = 450
        other_level = 700
        df["capacity"] = df.apply(
            lambda x: 100 * (1 - x["distance"] / drink_level)
            if x["kind"] == "D"
            else 100 * (1 - x["distance"] / other_level),
            axis=1,
        )
        df["capacity"] = df["capacity"].clip(0, 100)
        return df
