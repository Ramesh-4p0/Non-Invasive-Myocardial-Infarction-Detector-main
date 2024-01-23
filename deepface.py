
from deepface import DeepFace

obj = DeepFace.analyze(img_path = pt,
        actions = ['age', 'gender', 'race', 'emotion']
)

obj['emotion']

