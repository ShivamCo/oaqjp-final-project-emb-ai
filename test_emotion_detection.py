from EmotionDetection.emotion_detection import emotion_detector
import unittest

class test_emotion_detection(unittest.TestCase):

    def test_emotion_detection(self):

        result1 = emotion_detector("I am glad this happened")
        self.assertEqual(result1['dominant_emoiton'], 'joy')
        
        result2 = emotion_detector("I am really mad about this")
        self.assertEqual(result2['dominant_emoiton'], 'anger')
        
        result3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result3['dominant_emoiton'], 'disgust')
        
        result4 = emotion_detector("I am so sad about this")
        self.assertEqual(result4['dominant_emoiton'], 'sadness')
        
        result5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result5['dominant_emoiton'], 'fear')


unittest.main()

