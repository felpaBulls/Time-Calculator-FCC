def add_time(start_time, duration_time, day=''):
    start_time_list = start_time.split(':')

    start_hour = int(start_time_list[0])
    start_min = int(start_time_list[1][:2])
    start_AMPM = start_time_list[1][3:5]

    # paso de 12hs. a 24hs.
    if start_AMPM == 'PM':
        start_hour = start_hour + 12


    duration_time_list = duration_time.split(':')

    duration_hour = int(duration_time_list[0])
    duration_min = int(duration_time_list[1])

    # cuento las horas que se agregan
    finish_min = start_min + duration_min
    if finish_min > 60:
        finish_min = finish_min - 60
        cont_horas = 1
    else: cont_horas = 0

    finish_hour = start_hour + duration_hour + cont_horas

    # cuento los días que se agregan
    finish_day = 0
    while finish_hour >= 24:
        finish_hour = finish_hour - 24
        finish_day += 1

    # paso de 24hs. a 12hs.
    if finish_hour >= 12:
        finish_hour = finish_hour - 12
        finish_AMPM = 'PM'
    else: finish_AMPM = 'AM'

    # para que aparezca el 1er cero cuando min<10
    if finish_min < 10:
        finish_min = '0' + str(finish_min)

    # para que diga 12:07 AM en vez de 00:07 AM
    if finish_hour == 0:
        finish_hour = 12

    #acá entra si especifiqué un día de inicio
    if day != '':
        day = day.upper()
        days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']

        for i in range(len(days)):
            if day == days[i]:
                start_day = i

        finish_day_S = start_day + finish_day

        while finish_day_S >= 7:
            finish_day_S = finish_day_S - 7

        finish_day_S = days[finish_day_S]

        if finish_day == 0:
            finish_time = str(finish_hour) + ':' + str(finish_min) + ' ' + finish_AMPM + ', ' + finish_day_S[0] + finish_day_S[1:].lower()
            return finish_time

        if finish_day == 1:
            finish_time = str(finish_hour) + ':' + str(finish_min) + ' ' + finish_AMPM + ', ' + finish_day_S[0] + finish_day_S[1:].lower() + ' (next day)'
            return finish_time

        if finish_day > 1:
            finish_time = str(finish_hour) + ':' + str(finish_min) + ' ' + finish_AMPM + ', ' + finish_day_S[0] + finish_day_S[1:].lower() + ' (' + str(finish_day) + ' days later)'
            return finish_time


    if finish_day == 0:
        finish_time = str(finish_hour) + ':' + str(finish_min) +' '+ finish_AMPM

    if finish_day == 1:
        finish_time = str(finish_hour) + ':' + str(finish_min) +' '+ finish_AMPM + ' (next day)'

    if finish_day > 1:
        finish_time = str(finish_hour) + ':' + str(finish_min) +' '+ finish_AMPM + ' (' + str(finish_day) + ' days later)'


    return finish_time

print(add_time("11:43 PM", "24:20", "tueSday"))
