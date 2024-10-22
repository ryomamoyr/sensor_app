// frontend/src/components/SummaryTable.tsx

import React from 'react';
import './SummaryTable.css';

interface SummaryTableProps {
    summary: Array<Record<string, any>>;
}

const SummaryTable: React.FC<SummaryTableProps> = ({ summary }) => {
    if (summary.length === 0) return null;

    const headers = Object.keys(summary[0]);

    return (
        <div className="summary-table-container">
            <table>
                <thead>
                    <tr>
                        {headers.map(header => (
                            <th key={header}>{header}</th>
                        ))}
                    </tr>
                </thead>
                <tbody>
                    {summary.map((row, index) => (
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

export default SummaryTable;
