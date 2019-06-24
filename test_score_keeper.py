import unittest
import score_keeper 

class ScoreKeeperTest(unittest.TestCase):

    def setUp(self):
        score_keeper.clearAllScores()

    def testAddingScoreWhenZeroReturns1(self):
        score_keeper.addScore(1, 'target_1')
        scoreForTarget1 = score_keeper.getScoreForTarget('target_1')
        self.assertEqual(scoreForTarget1, 1)

    def testAdding_Score_With_2Hits_To_Same_Target_Returns_2(self):
        score_keeper.addScore(1, 'target_1')
        score_keeper.addScore(1, 'target_1')
        scoreForTarget1 = score_keeper.getScoreForTarget('target_1')
        self.assertEqual(scoreForTarget1, 2)

    def testAdding_1_to_Two_Different_Targets_Returns_1_For_Each(self):
        score_keeper.addScore(1, 'target_1')
        score_keeper.addScore(1, 'target_2')
        scoreForTarget1 = score_keeper.getScoreForTarget('target_1')
        scoreForTarget2 = score_keeper.getScoreForTarget('target_2')
        self.assertEqual(scoreForTarget1, 1)
        self.assertEqual(scoreForTarget2, 1)

    def testAdding_1_to_One_Target_And_2_to_A_Different_Target_Returns_Correct_Totals_For_Each(self):
        score_keeper.addScore(1, 'target_1')
        score_keeper.addScore(1, 'target_2')
        score_keeper.addScore(1, 'target_2')
        scoreForTarget1 = score_keeper.getScoreForTarget('target_1')
        scoreForTarget2 = score_keeper.getScoreForTarget('target_2')
        self.assertEqual(scoreForTarget1, 1)
        self.assertEqual(scoreForTarget2, 2)

    def testGetScoreForTargetNeverHitReturnsZero(self):
        value = score_keeper.getScoreForTarget("Notarealtarget")
        self.assertEqual(value, 0)