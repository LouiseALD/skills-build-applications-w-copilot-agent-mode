import octofit_tracker.models
print('Atributos do módulo models:', dir(octofit_tracker.models))
print('User:', getattr(octofit_tracker.models, 'User', None))
print('Team:', getattr(octofit_tracker.models, 'Team', None))
print('Activity:', getattr(octofit_tracker.models, 'Activity', None))
print('Leaderboard:', getattr(octofit_tracker.models, 'Leaderboard', None))
print('Workout:', getattr(octofit_tracker.models, 'Workout', None))
