import octofit_tracker.models2
print('Atributos do módulo models2:', dir(octofit_tracker.models2))
print('User:', getattr(octofit_tracker.models2, 'User', None))
print('Team:', getattr(octofit_tracker.models2, 'Team', None))
print('Activity:', getattr(octofit_tracker.models2, 'Activity', None))
print('Leaderboard:', getattr(octofit_tracker.models2, 'Leaderboard', None))
print('Workout:', getattr(octofit_tracker.models2, 'Workout', None))
