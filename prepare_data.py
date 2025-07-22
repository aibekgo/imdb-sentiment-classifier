# project/prepare_data.py

import os
import pandas as pd

def load_reviews_from_dir(dir_path, label):
    reviews = []
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        if os.path.isfile(file_path) and filename.endswith(".txt"):
            with open(file_path, encoding='utf-8') as f:
                reviews.append(f.read())
    return pd.DataFrame({'review': reviews, 'label': label})

def prepare_imdb_dataset(base_raw_path, save_path):
    train_pos = load_reviews_from_dir(os.path.join(base_raw_path, 'train/pos'), 1)
    train_neg = load_reviews_from_dir(os.path.join(base_raw_path, 'train/neg'), 0)
    test_pos = load_reviews_from_dir(os.path.join(base_raw_path, 'test/pos'), 1)
    test_neg = load_reviews_from_dir(os.path.join(base_raw_path, 'test/neg'), 0)

    df = pd.concat([train_pos, train_neg, test_pos, test_neg], ignore_index=True)
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    df.to_csv(save_path, index=False)
    print(f"✅ CSV сохранён по пути: {save_path}")
    print(df.head())

if __name__ == "__main__":
    RAW_PATH = "aclImdb"
    SAVE_PATH = "data/imdb_reviews.csv"
    prepare_imdb_dataset(RAW_PATH, SAVE_PATH)
