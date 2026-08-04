from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import KFold, cross_val_score
from pathlib import Path
from preprocessing import (
    load_dataset,
    create_engineered_features,
    select_features_target,
    encode_features,
    DEFAULT_FEATURES,
)

def save_cross_validation_metrics(scores):
    """Save Cross Validation metrics."""

    output_path = Path("outputs/metrics/cross_validation_metrics.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w") as file:
        file.write("========== K-Fold Cross Validation ==========\n\n")

        for i, score in enumerate(scores, start=1):
            file.write(f"Fold {i}: {score:.4f}\n")

        file.write("\n")
        file.write(f"Average R² : {scores.mean():.4f}\n")
        file.write(f"Std Dev    : {scores.std():.4f}\n")

    print(f"\nMetrics saved to: {output_path}")


def main():
    print("\n========== K-Fold Cross Validation ==========\n")

    # Load dataset
    df = load_dataset()

    # Apply Feature Engineering
    df = create_engineered_features(df)

    # Select features and target
    X, y = select_features_target(
        df,
        DEFAULT_FEATURES,
    )

    # Encode categorical features
    X_encoded, _, _ = encode_features(
        X,
        X,
    )

    # Best tuned Random Forest model
    model = RandomForestRegressor(
        n_estimators=200,
        max_depth=None,
        min_samples_split=2,
        min_samples_leaf=1,
        random_state=42,
        n_jobs=-1,
    )

    # 5-Fold Cross Validation
    kf = KFold(
        n_splits=5,
        shuffle=True,
        random_state=42,
    )

    scores = cross_val_score(
        estimator=model,
        X=X_encoded,
        y=y,
        cv=kf,
        scoring="r2",
        n_jobs=-1,
    )

    print("Fold R² Scores:")
    for i, score in enumerate(scores, start=1):
        print(f"Fold {i}: {score:.4f}")

    print("\nAverage R² :", f"{scores.mean():.4f}")
    print("Std Dev    :", f"{scores.std():.4f}")

    save_cross_validation_metrics(scores)


if __name__ == "__main__":
    main()