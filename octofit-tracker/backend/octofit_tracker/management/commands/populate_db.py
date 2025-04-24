from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from octofit_tracker.test_data import test_users, test_teams, test_activities, test_leaderboard, test_workouts
from datetime import timedelta, datetime

class Command(BaseCommand):
    help = 'Popula o banco octofit_db com dados de teste para users, teams, activity, leaderboard e workouts.'

    def handle(self, *args, **kwargs):
        # Limpa as coleções antes de popular
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Usuários
        for u in test_users:
            User.objects.create(email=u["email"], name=u["name"], password=u["password"])

        # Times
        for t in test_teams:
            Team.objects.create(name=t["name"], members=t["members"])

        # Atividades
        for a in test_activities:
            Activity.objects.create(
                user_email=a["user_email"],
                activity_type=a["type"],
                duration=timedelta(minutes=a["duration"]),
                date=datetime(2025, 4, 20, 8, 0)  # Data fixa para exemplo
            )

        # Leaderboard
        for l in test_leaderboard:
            Leaderboard.objects.create(user_email=l.get("team", l.get("user_email", "")), score=l["score"])

        # Workouts
        for w in test_workouts:
            Workout.objects.create(description=w["description"], suggested_for=w.get("suggested_for", "all"))

        self.stdout.write(self.style.SUCCESS('Banco octofit_db populado com dados de teste!'))
