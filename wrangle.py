from env import username, password, hostname
import numpy as np
import pandas as pd

class Wrangle:

    def get_data(self):
        """get_data creates dataframe from filename

        Returns:
            pandas dataframe: returns the curriculum logs dataframe
        """

        filename = "curriculum_logs.csv"

        return pd.read_csv(filename)

    def prep_data(self):
        """prep_data does some minor prep and feature engineering

        Returns:
            pandas dataframe: returns a prepped dataframe
        """

        df = Wrangle().get_data()

        df["program_name"] = np.where(df["program_id"] == 3, "data science", "web dev")

        df["date_time"] = pd.to_datetime(df['date'] + " " + df['time'])

        df = df.set_index(df["date_time"]).drop(["date", "time", "date_time"], axis=1)

        return df