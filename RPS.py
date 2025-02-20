# The example function below keeps track of the opponent's history and plays 
# whatever the opponent played two plays ago. It is not a very good player so 
# you will need to change the code to pass the challenge.

import tensorflow as tf # type: ignore
import numpy as np
import pandas as pd # type: ignore
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Create a sample dataset
data = {
    'move':      ['R', 'P', 'S', 'R', 'S', 'P', 'R', 'P', 'S', 'R', 'S', 'R', 'P', 'S'],
    'next_move': ['P', 'S', 'R', 'P', 'R', 'S', 'P', 'S', 'R', 'P', 'R', 'P', 'S', 'R']
}

df = pd.DataFrame(data)
df.to_csv('rock_paper_scissors.csv', index=False)

# print(df)

data = pd.read_csv('rock_paper_scissors.csv')

encoder = LabelEncoder()
data['move'] = encoder.fit_transform(data['move'])
data['next_move'] = encoder.transform(data['next_move'])

x = data['move'].values
y = data['next_move'].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

x_train = x_train.reshape(-1, 1)
x_test = x_test.reshape(-1, 1)

model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=3, output_dim=10),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
])

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    guess = "R"
    if len(opponent_history) > 2:
        guess = opponent_history[-2]

    return guess
