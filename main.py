# backend/main.py

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.dataloader.toilet import ToiletDataLoader
from backend.analyser.toilet import ToiletAnalyser
from backend.visualizer.toilet import ToiletVisualizer
from fastapi.responses import StreamingResponse, JSONResponse
import pandas as pd
import io
import logging
import json

# ロギングの設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# CORS 設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # フロントエンドのURL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/upload")
async def upload_files(files: list[UploadFile] = File(...)):
    if not files:
        logger.error("No files uploaded.")
        raise HTTPException(status_code=400, detail="ファイルが選択されていません。")

    data_loader = ToiletDataLoader()

    data_frames = []
    for file in files:
        content = await file.read()
        logger.info(f"Processing file: {file.filename}")
        try:
            # 受信したファイル内容を直接DataFrameとして読み込む
            df = pd.read_csv(io.StringIO(content.decode("utf-8")))
            data_frames.append(df)
            logger.info(f"Successfully read file: {file.filename}")
        except Exception as e:
            logger.error(f"Failed to read file {file.filename}: {str(e)}")
            raise HTTPException(
                status_code=400,
                detail=f"ファイル {file.filename} の読み込みに失敗しました。エラー: {str(e)}",
            )

    try:
        combined_data = data_loader.read_csv(data_frames)
        logger.info("Data loaded successfully.")
        # 'timestamp' 列は datetime 型のまま保持
    except Exception as e:
        logger.error(f"Data loading failed: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"データのロードに失敗しました。エラー: {str(e)}"
        )

    try:
        # ToiletAnalyser に combined_data を渡してインスタンス化
        analyser = ToiletAnalyser(combined_data)
        # 日次利用状況の要約と imos データを取得
        summary_df, imos_df = analyser.summarize_daily_usage()
        logger.info("Data analysis completed.")
        # 'start_time' と 'end_time' 列を文字列に変換
        summary_df["start_time"] = summary_df["start_time"].astype(str)
        summary_df["end_time"] = summary_df["end_time"].astype(str)
    except Exception as e:
        logger.error(f"Data analysis failed: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"データの分析に失敗しました。エラー: {str(e)}"
        )

    try:
        # ToiletVisualizer に summary_df を渡してインスタンス化
        visualizer = ToiletVisualizer(summary_df)
        # 各チャートを生成
        chart_usage_over_time = visualizer.plot_usage_over_time(imos_df)
        chart_usage_count_by_stall = visualizer.plot_usage_count_by_stall()
        logger.info("Data visualization completed.")
        # Plotly の図を JSON にシリアライズ
        chart_usage_over_time_json = json.loads(chart_usage_over_time.to_json())
        chart_usage_count_by_stall_json = json.loads(
            chart_usage_count_by_stall.to_json()
        )
    except Exception as e:
        logger.error(f"Data visualization failed: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"データの視覚化に失敗しました。エラー: {str(e)}"
        )

    try:
        # data_preview の 'timestamp' 列を文字列に変換
        data_preview = combined_data.head().copy()
        data_preview["timestamp"] = data_preview["timestamp"].astype(str)
    except Exception as e:
        logger.error(f"Data preview processing failed: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"データプレビューの処理に失敗しました。エラー: {str(e)}",
        )

    return JSONResponse(
        content={
            "data_preview": data_preview.to_dict(orient="records"),
            "summary": summary_df.to_dict(orient="records"),
            "charts": {
                "usage_over_time": chart_usage_over_time_json,
                "usage_count_by_stall": chart_usage_count_by_stall_json,
            },
        }
    )


@app.post("/download")
async def download_csv(summary: list[dict]):
    if not summary:
        raise HTTPException(status_code=400, detail="要約データが提供されていません。")

    df = pd.DataFrame(summary)
    csv_bytes = df.to_csv(index=False).encode("utf-8")
    return StreamingResponse(
        io.BytesIO(csv_bytes),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=daily_usage_summary.csv"},
    )
