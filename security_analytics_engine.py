import pandas as pd
import numpy as np

def generate_security_metrics(events):

    dataframe = pd.DataFrame(events)

    dataframe["high_risk"] = np.where(
        dataframe["anomaly_score"] > 75,
        1,
        0
    )

    return dataframe
