from django.core.management.base import BaseCommand
from octofit_tracker.test_data import test_users, test_teams, test_activities, test_leaderboard, test_workouts
import pymongo
from datetime import datetime

class Command(BaseCommand):
    help = 'Popula o banco octofit_db com dados de teste para users, teams, activities, leaderboard e workouts.'

    def handle(self, *args, **kwargs):
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        db = client['octofit_db']

        # Limpa as coleções
        for col in ['users', 'teams', 'activities', 'leaderboard', 'workouts']:
            db[col].delete_many({})

        # Popula usuários
        for u in test_users:
            db['users'].insert_one(u)

        # Popula times
        for t in test_teams:
            db['teams'].insert_one(t)

        # Popula atividades
        for a in test_activities:
            doc = {
                'user_email': a['user_email'],
                'activity_type': a['type'],
                'duration': a['duration'],
                'distance': a.get('distance', 0.0),
                'date': datetime(2025, 4, 20, 8, 0)
            }
            db['activities'].insert_one(doc)

        # Popula leaderboard
        for l in test_leaderboard:
            doc = {
                'team_name': l.get('team', ''),
                'score': l['score']
            }
            db['leaderboard'].insert_one(doc)

        # Popula workouts
        for w in test_workouts:
            doc = {
                'description': w['description'],
                'suggested_for': w.get('suggested_for', 'all')
            }
            db['workouts'].insert_one(doc)

        self.stdout.write(self.style.SUCCESS('Banco octofit_db populado com dados de teste via comando Django!'))
