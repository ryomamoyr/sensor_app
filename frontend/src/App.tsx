// frontend/src/App.tsx

import React, { useState } from 'react';
import FileUploader from './components/FileUploader';
import DataPreview from './components/DataPreview';
import SummaryTable from './components/SummaryTable';
import Charts from './components/Charts';
import DownloadButton from './components/DownloadButton';
import Footer from './components/Footer';
import Accordion from './components/Accordion'; // アコーディオンコンポーネントをインポート
import { AnalysisResult } from './interfaces';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import './App.css';

const App: React.FC = () => {
  const [analysisResult, setAnalysisResult] = useState<AnalysisResult | null>(null);

  const handleAnalysisComplete = (data: AnalysisResult) => {
    setAnalysisResult(data);
  };

  return (
    <div className="App">
      <header>
        <h1>トイレセンサデータ分析アプリ</h1>
      </header>
      <main>
        <FileUploader onAnalysisComplete={handleAnalysisComplete} />
        {analysisResult && (
          <>
            <DataPreview data={analysisResult.data_preview} />
            <div className="summary-and-charts">
              <Charts charts={analysisResult.charts} />
              <Accordion title="日次利用状況の要約">
                <SummaryTable summary={analysisResult.summary} />
              </Accordion>
            </div>
            <div className="download-section">
              <h2>分析結果のダウンロード</h2>
              <DownloadButton summary={analysisResult.summary} />
            </div>
          </>
        )}
      </main>
      <Footer />
      <ToastContainer position="top-right" autoClose={5000} hideProgressBar={false} />
    </div>
  );
};

export default App;
