// frontend/src/components/FileUploader.tsx

import React, { useState } from 'react';
import { uploadFiles } from '../api/api';
import { AnalysisResult } from '../interfaces';
import { toast } from 'react-toastify';
import Loader from './Loader'; // ローダーをインポート
import './FileUploader.css';

interface FileUploaderProps {
    onAnalysisComplete: (data: AnalysisResult) => void;
}

const FileUploader: React.FC<FileUploaderProps> = ({ onAnalysisComplete }) => {
    const [files, setFiles] = useState<FileList | null>(null);
    const [loading, setLoading] = useState<boolean>(false);

    const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setFiles(e.target.files);
    };

    const handleUpload = async () => {
        if (!files) {
            toast.error('ファイルが選択されていません。');
            return;
        }

        setLoading(true);
        try {
            const data = await uploadFiles(files);
            onAnalysisComplete(data);
            toast.success('データの分析が完了しました！');
        } catch (error: any) {
            console.error("Upload Error:", error);
            if (error.response) {
                // サーバーからのレスポンスがある場合
                toast.error(`エラー: ${error.response.data.detail}`);
            } else if (error.request) {
                // リクエストは送信されたがレスポンスがない場合
                toast.error('サーバーからのレスポンスがありません。');
            } else {
                // その他のエラー
                toast.error(`エラーが発生しました: ${error.message}`);
            }
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="file-uploader">
            {loading && <Loader />} {/* ローダーを表示 */}
            <input type="file" multiple accept=".csv" onChange={handleFileChange} />
            <button onClick={handleUpload} disabled={!files || loading}>
                {loading ? 'アップロード中...' : 'アップロード'}
            </button>
        </div>
    );
};

export default FileUploader;
