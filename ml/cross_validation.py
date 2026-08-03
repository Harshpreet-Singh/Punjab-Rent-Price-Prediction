from sklearn.model_selection import cross_val_score, KFold
from preprocessing import (
    load_dataset,
    create_engineered_features,
    select_features_target,
    encode_features,
    DEFAULT_FEATURES,
)

kf = KFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

def main():
    df = load_dataset()
    df = create_engineered_features(df)
    X, y = select_features_target(
        df,
        DEFAULT_FEATURES,
    )
    X_encoded, _, preprocessor = encode_features(X, X)

    scores = cross_val_score(
        model,
        X_encoded,
        y,
        cv=kf,
        scoring="r2",
        n_jobs=-1,
    )
    # Load data using preprocessing pipeline

    # Create tuned Random Forest

    # Create KFold

    # Run cross validation

    # Print fold scores

    # Print mean

    # Print standard deviation
    pass