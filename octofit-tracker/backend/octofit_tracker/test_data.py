# Dados de teste para o OctoFit Tracker (baseado no exemplo do Monafit Tracker)
# Salve como test_data.py

test_users = [
    {"email": "octohero1@mergington.edu", "password": "supersecure1", "name": "Octo Hero 1"},
    {"email": "octohero2@mergington.edu", "password": "supersecure2", "name": "Octo Hero 2"},
    {"email": "octohero3@mergington.edu", "password": "supersecure3", "name": "Octo Hero 3"},
]

test_teams = [
    {"name": "Team Kraken", "members": ["octohero1@mergington.edu", "octohero2@mergington.edu"]},
    {"name": "Team Coral", "members": ["octohero3@mergington.edu"]},
]

test_activities = [
    {"user_email": "octohero1@mergington.edu", "type": "run", "duration": 30, "distance": 5.0},
    {"user_email": "octohero2@mergington.edu", "type": "walk", "duration": 60, "distance": 4.0},
    {"user_email": "octohero3@mergington.edu", "type": "strength", "duration": 45, "distance": 0.0},
]

test_leaderboard = [
    {"team": "Team Kraken", "score": 120},
    {"team": "Team Coral", "score": 80},
]

test_workouts = [
    {"description": "5km corrida matinal"},
    {"description": "Treino de força para membros superiores"},
    {"description": "Caminhada leve de 4km"},
]
