// frontend/src/api/api.ts

import axios from 'axios';
import { AnalysisResult } from '../interfaces';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;
console.log("API_BASE_URL:", API_BASE_URL); // デバッグ用

export const uploadFiles = async (files: FileList): Promise<AnalysisResult> => {
    const formData = new FormData();
    Array.from(files).forEach(file => {
        formData.append('files', file);
    });

    try {
        const response = await axios.post<AnalysisResult>(`${API_BASE_URL}/upload`, formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
            },
        });
        return response.data;
    } catch (error) {
        console.error("Upload Error:", error); // エラーログを追加
        throw error;
    }
};

export const downloadCSV = async (summary: Array<Record<string, any>>): Promise<Blob> => {
    const response = await axios.post(`${API_BASE_URL}/download`, summary, {
        responseType: 'blob',
    });

    return response.data;
};
