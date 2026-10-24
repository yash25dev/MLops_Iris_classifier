# Testing Strategy

This document outlines the unit testing strategy, layers covered, and code coverage percentages for the MLops Iris Classifier project.

## Summary
* **Total Automated Tests:** 16 passed
* **Overall Source Code Coverage:** 19%
* **Platform:** Win32, Python 3.11.9-final-0

## Test Suite Mapping

| Test File | Layer Covered | Source File Target | Coverage % |
| :--- | :--- | :--- | :--- |
| `tests/test_preprocess.py` | Data Preprocessing | `src/pipeline/preprocess.py` | 83% |
| `tests/test_validate.py` | Pipeline Validation | `src/pipeline/validate.py` | 76% |
| `tests/test_features.py` | Feature Engineering | `src/pipeline/features.py` | 75% |
| `tests/test_model_quality.py` | Model Quality | `src/baseline_model.py` / `src/compare_tuning_results.py` | 0% |
| `tests/test_training_pipeline.py`| Pipeline Training | `src/train.py` / `src/train_with_mlflow.py` | 0% |

## Verification Notes
* All edge cases from steps 2-4 are covered.
* Key core pipeline modules (`preprocess.py`, `features.py`, `validate.py`) successfully show high functional coverage (above 75%).
