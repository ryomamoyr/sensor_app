import pandas as pd


class ToiletAnalyser:
    def __init__(self, input_df: pd.DataFrame):
        self.input_df = input_df

    def summarize_daily_usage(self) -> (pd.DataFrame, pd.DataFrame):
        """全ての個室の利用結果を表すDataFrameを作成する"""
        result_df_list = []
        input_df = self.input_df
        for macaddress in input_df["macaddress"].unique():
            df = self._generate_usage_details(input_df, macaddress)
            result_df_list.append(df)
        result_df = pd.concat(result_df_list)
        result_df.reset_index(drop=True, inplace=True)
        return result_df

    def _generate_usage_details(
        self, input_df: pd.DataFrame, macaddress: str
    ) -> pd.DataFrame:
        """各個室の利用結果を表すDataFrameを作成する
        Args:
            input_df (pd.DataFrame): ToiletDataLoaderで読み込んだデータ
            macadress (str): 個室名
            date (datetime): 日付

        Returns:
            pd.DataFrame: 利用結果を表すDataFrame

        Algorithm:
            2. 指定した個室のデータを抽出
            3. 指定した個室のデータのうち、7時から23時までのデータを抽出
            4. is_hall_sensor_closedの差分を取り、0でない行を抽出
            5. 差分が-1から始まる場合、最初の行を削除
            6. 開始時間のデータを抽出
            7. 終了時間のデータを抽出
            8. 開始時間と終了時間の差を取り、利用時間を算出
            9. 利用結果を表すDataFrameを作成
        """
        df = input_df[input_df["macaddress"] == macaddress]
        df = df[(df.timestamp.dt.hour >= 7) & (df.timestamp.dt.hour <= 23)]
        df["diff"] = df["is_hall_sensor_closed"].diff()
        df = df[df["diff"] != 0]
        df = df[df["diff"].notnull()]
        df.reset_index(drop=True, inplace=True)
        if len(df) > 0 and df.iloc[0]["diff"] == -1:
            df.drop(index=0, inplace=True)
        df_start = df[df["is_hall_sensor_closed"] == 1].reset_index(drop=True)
        df_end = df[df["is_hall_sensor_closed"] == 0].reset_index(drop=True)
        length = len(df_start)
        df_end = df_end.iloc[-length:]
        result_df = pd.DataFrame(
            {
                "macaddress": macaddress,
                "start_time": df_start["timestamp"],
                "end_time": df_end["timestamp"],
                "usage_time": (
                    df_end["timestamp"] - df_start["timestamp"]
                ).dt.total_seconds(),
            }
        )
        # 利用時間が正の値のみを残す
        result_df = result_df[result_df["usage_time"] > 0].reset_index(drop=True)
        return result_df

    def make_imos_df(self, result_df: pd.DataFrame) -> pd.DataFrame:
        """時間断面のトイレの累積仕様台数をimos法で作成する"""
        result_df["start_time"] = result_df["start_time"].dt.round("1min")
        result_df["end_time"] = result_df["end_time"].dt.round("1min")
        result_df.drop_duplicates(inplace=True)
        result_df.reset_index(drop=True, inplace=True)
        result_df.dropna(inplace=True)
        start_time = result_df["start_time"].min()
        end_time = result_df["end_time"].max()
        # imos法のための時間軸を作成
        time_index = pd.date_range(start=start_time, end=end_time, freq="1min")
        imos = pd.Series(0, index=time_index)
        # トイレの利用開始時間と終了時間をimos法で集計
        for i, row in result_df.iterrows():
            imos.loc[row["start_time"]] += 1
            imos.loc[row["end_time"]] -= 1
        imos_df = imos.cumsum().to_frame(name="usage_count")
        return imos_df