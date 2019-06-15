import unittest
import score_keeper 

class ScoreKeeperTest(unittest.TestCase):

    def testAddingScoreWhenZeroReturns1(self):
        score_keeper.addScore(1, 'target_1')
        x = score_keeper.getScoreForTarget('target_1')
        self.assertTrue(x == 1)
    def testCanary(self):
        self.assertTrue(True)