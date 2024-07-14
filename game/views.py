import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Game

def check_winner(board):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != ' ':
            return board[combo[0]]
    if ' ' not in board:
        return 'Finish'  # Tie
    return None

@csrf_exempt
def new_game(request):
    if request.method == 'POST':
        game = Game()
        game.save()
        return JsonResponse({'game_id': game.id, 'board': game.board, 'current_player': game.current_player})

@csrf_exempt
def make_move(request, game_id):
    if request.method == 'POST':
        game = Game.objects.get(pk=game_id)
        if game.game_over:
            return JsonResponse({'Game is finished, the winner was:': game.winner})
        try:
            data = json.loads(request.body)
            position = data.get('position')

            if position is None or not (0 <= position < 9):
                return JsonResponse({'error': 'Invalid position'}, status=400)

            if game.board[position] != ' ' or game.game_over:
                return JsonResponse({'error': 'Invalid move'}, status=400)

            board = list(game.board)
            board[position] = game.current_player
            game.board = ''.join(board)

            winner = check_winner(game.board)
            if winner:
                game.winner = winner
                game.game_over = True
            else:
                game.current_player = 'O' if game.current_player == 'X' else 'X'

            game.save()
            return JsonResponse({'game_id': game.id, 'board': game.board, 'current_player': game.current_player, 'winner': game.winner, 'game_over': game.game_over})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
