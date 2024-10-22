// frontend/src/components/Charts.tsx

import React from 'react';
import Plot from 'react-plotly.js';
import './Charts.css';

interface ChartsProps {
    charts: {
        usage_over_time: any;
        usage_count_by_stall: any;
    };
}

const Charts: React.FC<ChartsProps> = ({ charts }) => {
    return (
        <div className="charts-container">
            <div className="chart-wrapper">
                <h2>時間帯ごとのトイレ利用台数</h2>
                <Plot
                    data={charts.usage_over_time.data}
                    layout={{
                        ...charts.usage_over_time.layout,
                        autosize: true,
                        paper_bgcolor: '#1E1E1E',
                        plot_bgcolor: '#1E1E1E',
                        font: { color: '#FFFFFF' },
                        margin: { t: 50, l: 50, r: 50, b: 50 }
                    }}
                    useResizeHandler={true}
                    style={{ width: '100%', height: '100%' }}
                />
            </div>
            <div className="chart-wrapper">
                <h2>個室ごとの利用回数</h2>
                <Plot
                    data={charts.usage_count_by_stall.data}
                    layout={{
                        ...charts.usage_count_by_stall.layout,
                        autosize: true,
                        paper_bgcolor: '#1E1E1E',
                        plot_bgcolor: '#1E1E1E',
                        font: { color: '#FFFFFF' },
                        margin: { t: 50, l: 50, r: 50, b: 50 }
                    }}
                    useResizeHandler={true}
                    style={{ width: '100%', height: '100%' }}
                />
            </div>
        </div>
    );
};

export default Charts;
