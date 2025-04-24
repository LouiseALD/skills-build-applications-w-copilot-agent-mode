import octofit_tracker.models3
print('Atributos do módulo models3:', dir(octofit_tracker.models3))
print('User:', getattr(octofit_tracker.models3, 'User', None))
print('Team:', getattr(octofit_tracker.models3, 'Team', None))
print('Activity:', getattr(octofit_tracker.models3, 'Activity', None))
print('Leaderboard:', getattr(octofit_tracker.models3, 'Leaderboard', None))
print('Workout:', getattr(octofit_tracker.models3, 'Workout', None))
