# 実装方法

## 1. Streamlitでの起動

### 最も簡単な実装方法

```bash
streamlit run ./streamlit/app.py
```

## 2. ReactとFastAPIを使用した実装

### 1. Backendの起動 (FastAPI)

プロジェクトのルートディレクトリで以下のコマンドを実行します。

```bash
uvicorn main:app --reload
```

### 2. Frontendの起動 (React)

以下の手順でReactアプリを起動します。

```bash
cd frontend
npm run dev
```

これでFrontendとBackendの両方が起動するはず。


