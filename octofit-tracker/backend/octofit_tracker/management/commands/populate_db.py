from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from octofit_tracker.test_data import test_users, test_teams, test_activities, test_leaderboard, test_workouts
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Popula o banco octofit_db com dados de teste para users, teams, activities, leaderboard e workouts.'

    def handle(self, *args, **kwargs):
        # Limpa as coleções
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Popula usuários
        for u in test_users:
            User.objects.create(email=u['email'], name=u['name'], password=u['password'])

        # Popula times
        for t in test_teams:
            Team.objects.create(name=t['name'], members=t['members'])

        # Popula atividades
        for a in test_activities:
            Activity.objects.create(
                user_email=a['user_email'],
                activity_type=a['type'],
                duration=timedelta(minutes=a['duration']),
                date=datetime(2025, 4, 20, 8, 0)
            )

        # Popula leaderboard
        for l in test_leaderboard:
            Leaderboard.objects.create(user_email=l.get('team', ''), score=l['score'])

        # Popula workouts
        for w in test_workouts:
            Workout.objects.create(description=w['description'], suggested_for=w.get('suggested_for', 'all'))

        self.stdout.write(self.style.SUCCESS('Banco octofit_db populado com dados de teste!'))
