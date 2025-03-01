from datetime import datetime

def datetime_long_formater(json):
    formated_date = datetime.fromisoformat(json)
    long_datetime = formated_date.strftime('%d/%m/%Y às %H:%M')
    return long_datetime

    