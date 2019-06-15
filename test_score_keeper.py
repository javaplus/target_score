import unittest
import score_keeper 

class ScoreKeeperTest(unittest.TestCase):

    def setUp(self):
        score_keeper.clearAllScores()

    def testAddingScoreWhenZeroReturns1(self):
        score_keeper.addScore(1, 'target_1')
        x = score_keeper.getScoreForTarget('target_1')
        self.assertEqual(x, 1)

    def testAdding_Score_With_2Hits_To_Same_Target_Returns_2(self):
        score_keeper.addScore(1, 'target_1')
        score_keeper.addScore(1, 'target_1')
        x = score_keeper.getScoreForTarget('target_1')
        self.assertEqual(x, 2)

    def testCanary(self):
        self.assertTrue(True)