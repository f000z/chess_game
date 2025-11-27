from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum, Count, Q
from game.models import Game
from players.models import Player
from score.models import Score

class GameLeaderboardView(APIView):
    def get(self, request):
        game_id = request.query_params.get('game_id')
        if not game_id:
            return Response({"error":"game_id is required"}, status=400)
        try:
            game = Game.objects.get(id=game_id)
        except Game.DoesNotExist:
            return Response({"error":"Game not found."}, status=404)

        agg = Score.objects.filter(game=game).values('player','player__nickname','player__country').annotate(
            points=Sum('points'),
            wins=Count('id', filter=Q(result='win')),
            draws=Count('id', filter=Q(result='draw')),
            losses=Count('id', filter=Q(result='loss'))
        ).order_by('-points')

        leaderboard = []
        rank = 1
        for a in agg:
            player_obj = Player.objects.get(id=a['player'])
            leaderboard.append({
                "rank": rank,
                "player": a['player__nickname'],
                "player_id": a['player'],
                "country": a['player__country'],
                "rating": player_obj.rating,
                "points": a['points'] or 0,
                "wins": a['wins'],
                "draws": a['draws'],
                "losses": a['losses'],
                "rating_change": a['points'] or 0
            })
            rank += 1

        return Response(leaderboard)

class TopPlayersLeaderboardView(APIView):
    def get(self, request):
        game_id = request.query_params.get('game_id')
        limit = int(request.query_params.get('limit', 10))
        if not game_id:
            return Response({"error":"game_id is required"}, status=400)
        try:
            game = Game.objects.get(id=game_id)
        except Game.DoesNotExist:
            return Response({"error":"Game not found."}, status=404)

        agg = Score.objects.filter(game=game).values('player__nickname','player__country','player').annotate(points=Sum('points')).order_by('-points')[:min(limit,50)]
        results = []
        for idx, a in enumerate(agg, start=1):
            results.append({
                "rank": idx,
                "player": a['player__nickname'],
                "country": a['player__country'],
                "rating": Player.objects.get(id=a['player']).rating,
                "points": a['points'] or 0
            })
        return Response({
            "game_id": game.id,
            "game_title": game.title,
            "limit": limit,
            "total_players": Score.objects.filter(game=game).values('player').distinct().count(),
            "leaderboard": results
        })

class GlobalLeaderboardView(APIView):
    def get(self, request):
        country = request.query_params.get('country')
        limit = int(request.query_params.get('limit', 100))
        qs = Player.objects.all()
        if country:
            qs = qs.filter(country__iexact=country)
        qs = qs.order_by('-rating')[:min(limit,500)]
        data = []
        for idx, p in enumerate(qs, start=1):
            total_games = p.scores.count()
            data.append({
                "rank": idx,
                "player": p.nickname,
                "rating": p.rating,
                "total_games": total_games
            })
        return Response({
            "total_players": qs.count(),
            "country": country,
            "leaderboard": data
        })
