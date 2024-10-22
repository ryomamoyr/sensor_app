// frontend/src/components/DownloadButton.tsx

import React from 'react';
import { downloadCSV } from '../api/api';
import { toast } from 'react-toastify';
import './DownloadButton.css';

interface DownloadButtonProps {
    summary: Array<Record<string, any>>;
}

const DownloadButton: React.FC<DownloadButtonProps> = ({ summary }) => {
    const handleDownload = async () => {
        try {
            const blob = await downloadCSV(summary);
            const url = window.URL.createObjectURL(new Blob([blob]));
            const link = document.createElement('a');
            link.href = url;
            link.setAttribute('download', 'daily_usage_summary.csv');
            document.body.appendChild(link);
            link.click();
            link.parentNode?.removeChild(link);
            toast.success('CSVファイルをダウンロードしました。');
        } catch (error) {
            console.error("Download Error:", error);
            toast.error('CSVファイルのダウンロードに失敗しました。');
        }
    };

    return (
        <button className="download-button" onClick={handleDownload}>
            ダウンロード
        </button>
    );
};

export default DownloadButton;
