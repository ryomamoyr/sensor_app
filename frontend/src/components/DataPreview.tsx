// frontend/src/components/DataPreview.tsx

import React from 'react';
import './DataPreview.css';

interface DataPreviewProps {
    data: Array<Record<string, any>>;
}

const DataPreview: React.FC<DataPreviewProps> = ({ data }) => {
    if (data.length === 0) return null;

    const headers = Object.keys(data[0]);

    return (
        <div className="data-preview-container">
            <h2>アップロードされたデータのプレビュー</h2>
            <table>
                <thead>
                    <tr>
                        {headers.map(header => (
                            <th key={header}>{header}</th>
                        ))}
                    </tr>
                </thead>
                <tbody>
                    {data.map((row, index) => (
                        <tr key={index}>
                            {headers.map(header => (
                                <td key={header}>{row[header]}</td>
                            ))}
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default DataPreview;
