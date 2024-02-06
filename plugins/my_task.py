import pickle
import joblib
import os
class MyTask:
    def __init__(self, chromastft, rms, spectral_centroid, spectral_bandwidth, spectral_rolloff, zero_crossing_rate, mfcc_1, mfcc_2, mfcc_3, mfcc_4, mfcc_5, mfcc_6, mfcc_7, mfcc_8, mfcc_9, mfcc_10, mfcc_11, mfcc_12, mfcc_13, mfcc_14, mfcc_15, mfcc_16, mfcc_17, mfcc_18, mfcc_19, mfcc_20):
        self.chromastft = float(chromastft)
        self.rms = float(rms)
        self.spectral_centroid = float(spectral_centroid)
        self.spectral_bandwidth = float(spectral_bandwidth)
        self.spectral_rolloff = float(spectral_rolloff)
        self.zero_crossing_rate = float(zero_crossing_rate)
        self.mfcc_1 = float(mfcc_1)
        self.mfcc_2 = float(mfcc_2)
        self.mfcc_3 = float(mfcc_3)
        self.mfcc_4 = float(mfcc_4)
        self.mfcc_5 = float(mfcc_5)
        self.mfcc_6 = float(mfcc_6)
        self.mfcc_7 = float(mfcc_7)
        self.mfcc_8 = float(mfcc_8)
        self.mfcc_9 = float(mfcc_9)
        self.mfcc_10 = float(mfcc_10)
        self.mfcc_11 = float(mfcc_11)
        self.mfcc_12 = float(mfcc_12)
        self.mfcc_13 = float(mfcc_13)
        self.mfcc_14 = float(mfcc_14)
        self.mfcc_15 = float(mfcc_15)
        self.mfcc_16 = float(mfcc_16)
        self.mfcc_17 = float(mfcc_17)
        self.mfcc_18 = float(mfcc_18)
        self.mfcc_19 = float(mfcc_19)
        self.mfcc_20 = float(mfcc_20)

    def get_features(self):
        return [self.chromastft, self.rms, self.spectral_centroid, self.spectral_bandwidth,
                self.spectral_rolloff, self.zero_crossing_rate, self.mfcc_1, self.mfcc_2, self.mfcc_3,
                self.mfcc_4, self.mfcc_5, self.mfcc_6, self.mfcc_7, self.mfcc_8, self.mfcc_9, self.mfcc_10,
                self.mfcc_11, self.mfcc_12, self.mfcc_13, self.mfcc_14, self.mfcc_15, self.mfcc_16, self.mfcc_17,
                self.mfcc_18, self.mfcc_19, self.mfcc_20]
    def my_function(self):
        features = self.get_features()
        try:
            model = joblib.load(open('/opt/airflow/dags/model.pkl', 'rb'))
            prediction = model.predict([features])
            if prediction==0:
                return "Prediction Result: The Song is Unpopular"
            else:
                return "Prediction Result: The Song is Popular"
        except FileNotFoundError:
            return f"Error: Model file not found "
        except Exception as e:
            return f"Error "

