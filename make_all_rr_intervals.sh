#!/usr/bin/env sh

source env/bin/activate;
export DATA_PATH=/data/extracts_parquet;
export EXPORT_PATH=/data;
# python3 src/usecase/detect_qrs.py --qrs-file-path $DATA_PATH/ecg.01-002.parquet --method hamilton  --output-folder $EXPORT_PATH/1_rr_inteverals/;
# python3 src/usecase/detect_qrs.py --qrs-file-path $DATA_PATH/ecg.01-003.parquet --method hamilton  --output-folder $EXPORT_PATH/1_rr_inteverals/;
# python3 src/usecase/detect_qrs.py --qrs-file-path $DATA_PATH/ecg.01-004.parquet --method hamilton  --output-folder $EXPORT_PATH/1_rr_inteverals/;
# python3 src/usecase/detect_qrs.py --qrs-file-path $DATA_PATH/ecg.01-005.parquet --method hamilton  --output-folder $EXPORT_PATH/1_rr_inteverals/;
# python3 src/usecase/detect_qrs.py --qrs-file-path $DATA_PATH/ecg.01-006.parquet --method hamilton  --output-folder $EXPORT_PATH/1_rr_inteverals/;
# python3 src/usecase/detect_qrs.py --qrs-file-path $DATA_PATH/ecg.01-007.parquet --method hamilton  --output-folder $EXPORT_PATH/1_rr_inteverals/;
# python3 src/usecase/detect_qrs.py --qrs-file-path $DATA_PATH/ecg.01-008.parquet --method hamilton  --output-folder $EXPORT_PATH/1_rr_inteverals/;
# python3 src/usecase/detect_qrs.py --qrs-file-path $DATA_PATH/ecg.01-009.parquet --method hamilton  --output-folder $EXPORT_PATH/1_rr_inteverals/;
# python3 src/usecase/detect_qrs.py --qrs-file-path $DATA_PATH/ecg.01-010.parquet --method hamilton  --output-folder $EXPORT_PATH/1_rr_inteverals/;

python3 src/usecase/compute_hrvanalysis_features.py --rr-intervals-file-path /data/1_rr_inteverals/rr_01-002.csv --output-folder $(EXPORT_PATH)/2_hrv_features/;
python3 src/usecase/compute_hrvanalysis_features.py --rr-intervals-file-path /data/1_rr_inteverals/rr_01-003.csv --output-folder $(EXPORT_PATH)/2_hrv_features/;
python3 src/usecase/compute_hrvanalysis_features.py --rr-intervals-file-path /data/1_rr_inteverals/rr_01-004.csv --output-folder $(EXPORT_PATH)/2_hrv_features/;
python3 src/usecase/compute_hrvanalysis_features.py --rr-intervals-file-path /data/1_rr_inteverals/rr_01-005.csv --output-folder $(EXPORT_PATH)/2_hrv_features/;
python3 src/usecase/compute_hrvanalysis_features.py --rr-intervals-file-path /data/1_rr_inteverals/rr_01-006.csv --output-folder $(EXPORT_PATH)/2_hrv_features/;
python3 src/usecase/compute_hrvanalysis_features.py --rr-intervals-file-path /data/1_rr_inteverals/rr_01-007.csv --output-folder $(EXPORT_PATH)/2_hrv_features/;
python3 src/usecase/compute_hrvanalysis_features.py --rr-intervals-file-path /data/1_rr_inteverals/rr_01-008.csv --output-folder $(EXPORT_PATH)/2_hrv_features/;
python3 src/usecase/compute_hrvanalysis_features.py --rr-intervals-file-path /data/1_rr_inteverals/rr_01-009.csv --output-folder $(EXPORT_PATH)/2_hrv_features/;
python3 src/usecase/compute_hrvanalysis_features.py --rr-intervals-file-path /data/1_rr_inteverals/rr_01-010.csv --output-folder $(EXPORT_PATH)/2_hrv_features/;
