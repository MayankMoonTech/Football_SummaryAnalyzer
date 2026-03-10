import numpy as np

def calculate_xg(df):

    shots = df[df["event_type"]=="shot"]

    xg_values = []

    for _,shot in shots.iterrows():

        distance = np.sqrt((100-shot["x"])**2 + (50-shot["y"])**2)

        xg = 1/(1+np.exp(distance/10))

        xg_values.append(xg)

    shots["xG"] = xg_values

    return shots