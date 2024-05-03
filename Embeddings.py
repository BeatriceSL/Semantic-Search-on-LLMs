# !pip install cohere umap-learn altair datasets
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
import cohere
co = cohere.Client(os.environ['COHERE_API_KEY'])
import pandas as pd
three_words = pd.DataFrame({'text':
  [
      'sweet',
      'candy',
      'sugar',
      'lolipop',
  ]})

three_words
