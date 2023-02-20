from firebase import firebase
import datetime

fb = firebase.FirebaseApplication('enter your link here ',None)


def postData(name, time):
    data = {
        'Name': name,
        'Time': time
    }

    dateToday = datetime.date.today().strftime('%Y-%m-%d')
    #print(dateToday)
    fb.post(f'/{dateToday}',data)

if __name__ == "__main__":
    postData('Jhon', '65')
