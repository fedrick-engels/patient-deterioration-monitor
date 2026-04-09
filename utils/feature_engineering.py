import numpy as np

def compute_features(records):
    hr = [r['heart_rate'] for r in records]

    return {
        "hr_mean": np.mean(hr),
        "hr_std": np.std(hr),
        "hr_slope": (hr[-1] - hr[0]) / len(hr),
        "hr_abnormal": sum([1 for x in hr if x > 120 or x < 50])
    }