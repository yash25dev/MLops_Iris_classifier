# Feature Store Analysis

## Observed Benefits of the Feature Store

### 1. Elimination of Training-Serving Skew

The same feature definitions are registered in the Feast feature repository and can be used for both online and offline feature retrieval.

The `iris_engineered_features` FeatureView contains the engineered Iris features:

- `sepal_area`
- `petal_area`
- `sepal_to_petal_length_ratio`
- `petal_length_bin`

Using the same registered feature definitions for online and offline retrieval reduces the need to independently reimplement feature transformations for training and serving.

### 2. Feature Reusability

The registered Iris features can be reused by different workflows without recreating the feature engineering logic.

The `iris_feature_service` groups the Iris feature views and provides a reusable interface for consuming the registered features.

The same registered features can therefore be consumed by different models or workflows.

### 3. Centralized Governance

The feature repository provides a centralized location for defining and managing the features used by the Iris models.

The `features.py` file contains the entity, data source, feature views, and feature service definitions.

This provides a single source of truth for the feature definitions and makes the features easier to maintain and reuse across consuming models.

## Practical Verification

The following checks were performed during the experiment:

- `feast apply` successfully registered/updated the Iris entity and feature views.
- `feast feature-views list` showed:
  - `iris_measurements`
  - `iris_engineered_features`
- Both Iris feature views were reported as `AVAILABLE_ONLINE`.
- The Iris feature source was written to `data/iris_features.parquet`.
- Feast materialization was performed to populate the online store.
- Online feature retrieval was used to retrieve registered Iris features by `sample_id`.
- Historical/offline feature retrieval was used to retrieve features using event timestamps.
- The feature service `iris_feature_service` provides a reusable collection of the registered Iris features.

## Conclusion

The experiment demonstrates how a feature store provides a centralized system for defining, registering, storing, and retrieving machine-learning features.

For the Iris classification workflow, Feast provides:

1. Consistent feature definitions for online and offline use.
2. Reusable registered features for different ML workflows.
3. Centralized management of feature definitions.
4. Online feature retrieval for inference.
5. Historical feature retrieval for training and analysis.