import csv

from models_2 import PlayerLevel, LevelPrize


def award_prize(player_level, prize):
    player_level = PlayerLevel.objects.get(id=player_level.id)
    if player_level.is_completed:
        LevelPrize.objects.create(level=player_level, prize=prize, received=player_level.completed)


def make_stats():
    player_levels = PlayerLevel.objects.iterator()

    with open('stats.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')

        writer.writerow(['ID игрока', 'Название уровня', 'Пройден ли уровень', 'Полученный приз за уровень'])

        batch_size = 1000
        batch = []
        for player_level in player_levels:
            prize = LevelPrize.objects.filter(level=player_level).first()
            batch.append([player_level.player_id,
                          player_level.title,
                          player_level.is_completed,
                          prize.title
                          ])
            if len(batch) == batch_size:
                writer.writerows(batch)
                batch = []
        # Если записано не все значит batch не пуст и длина меньше batch_size
        if batch:
            writer.writerows(batch)
