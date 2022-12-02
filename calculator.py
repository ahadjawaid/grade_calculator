class Grades:
    def __init__(self, grading_scale, scores, scores_weight):
        self.scores = scores
        self.scores_weight = scores_weight
        self.grading_scale = grading_scale
        self.points = self._getCurrentPoints()
        self.letter_grade = self._getLetterGradeWithPoints(self.points)

    def _getCurrentPoints(self):
        current_points = 0
        for key in self.scores:
            for i in range(len(self.scores[key])):
                current_points += self.scores[key][i] * self.scores_weight[key][i]
        
        return current_points

    def _getValueForLetter(self, letter):
        for key in self.grading_scale:
            if self.grading_scale[key] == letter:
                return key     

    def _getLetterGradeWithPoints(self, points):
        range_values = sorted(list(self.grading_scale.keys()))
        range_val = max(range_values)

        for i in range(1, len(range_values)):
            if points < range_values[i]:
                return  self.grading_scale[range_values[i-1]]
                
        return self.grading_scale[range_val]

    def getScoreNeededForItem(self, key, index, goal):
        item_weight = self.scores_weight[key][index]
        goal_points = self._getValueForLetter(goal)
        points_needed = goal_points - self.points
        score_needed = points_needed / item_weight

        return score_needed
    
    def letterGradesPossibleForItem(self, key, index):
        score_needed = {}
        for letter in self.grading_scale.values():
            score = self.getScoreNeededForItem(key, index, letter)
            if 0 <= score <= 100:
                score_needed[letter] = score

        return score_needed