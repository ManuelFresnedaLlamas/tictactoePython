from django.test import TestCase
from .models import Game


class GameTests(TestCase):
    def test_create_game(self):
        response = self.client.post('/new/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('game_id', response.json())

    def test_make_move(self):
        response = self.client.post('/new/')
        game_id = response.json()['game_id']

        response = self.client.post(f'/move/{game_id}/', {'position': 0}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['board'][0], 'X')

        response = self.client.post(f'/move/{game_id}/', {'position': 1}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['board'][1], 'O')

    def test_invalid_move(self):
        response = self.client.post('/new/')
        game_id = response.json()['game_id']

        response = self.client.post(f'/move/{game_id}/', {'position': 0}, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        response = self.client.post(f'/move/{game_id}/', {'position': 0}, content_type='application/json')
        self.assertEqual(response.status_code, 400)
