// frontend/src/interfaces/index.ts

export interface AnalysisResult {
    data_preview: Array<Record<string, any>>;
    summary: Array<Record<string, any>>;
    charts: {
        usage_over_time: any;
        usage_count_by_stall: any;
    };
}
