import pandas as pd


class SentimentClassifier:
   
   def __init__(self, path):
      
      self.path = path
      self.data_frame = None
      self.good_labels = pd.DataFrame(None, columns = ["id", "tweets", "labels"])
      self.bad_labels = pd.DataFrame(None, columns = ["id", "tweets", "labels"])
      self.neutral_labels = pd.DataFrame(None, columns = ["id", "tweets", "labels"])
   
   
   def load_data(self):
      
      self.data_frame = pd.read_csv(self.path)
   
   
   def classify_sentiment(self):
      
      self.good_labels = self.data_frame[self.data_frame['labels'] == 'good']
      self.bad_labels = self.data_frame[self.data_frame['labels'] == 'bad']
      self.neutral_labels = self.data_frame[self.data_frame['labels'] == 'neutral']
      
      print(self.good_labels)      
      print(self.neutral_labels)      
      print(self.bad_labels)      
   
           
   def save_to_csv(self):
      
      self.good_labels.to_csv("Praktikum/data_dest/sentiment_good.csv", index=False)
      self.bad_labels.to_csv("Praktikum/data_dest/sentiment_bad.csv", index=False)
      self.neutral_labels.to_csv("Praktikum/data_dest/sentiment_neutral.csv", index=False)
   
   
   def summarize_counts(self):
      
      self.sentiment_counts = pd.DataFrame({
         'labels': ['good', 'bad', 'neutral'],
         'count': [len(self.good_labels), len(self.bad_labels), len(self.neutral_labels)]
      })
      self.sentiment_counts.to_csv("Praktikum/data_dest/sentiment_counts.csv")
   
   
if __name__ == "__main__":
   
   path = 'Praktikum/data_source/file.csv'
   classified_sentiment = SentimentClassifier(path)
   classified_sentiment.load_data()
   classified_sentiment.classify_sentiment()
   classified_sentiment.save_to_csv()
   classified_sentiment.summarize_counts()