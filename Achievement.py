#Achievement
class Achievement:
	def __init__(self):
		self.achieved = False
		self.name = ""

class TimeAchievement(Achievement):
	def __init__(self, time_needed):
		self.Achievement.__init__()
		self.time_required = time_needed

class CravingsAchievement(Achievement):
	def __init__(self, cravings_needing_beating):
		self.Achievement.__init__()
		self.cravings_to_beat = cravings_needing_beating

class PersonalBest(Achievement):
	def __init__(self, cravings_needing_beating):
		self.Achievement.__init__()

	def update_personal_best(self):
		pass

