#Media das notas


notas = [5.0, 7.5, 6.5, 6.0]

media = sum(notas) / len(notas)
print(f'Media total das notas: {media}')

notas_maiores_que_media = [notas for notas in notas if notas > media]
print(f'As notas maiores que a maedia sao: {notas_maiores_que_media}')
