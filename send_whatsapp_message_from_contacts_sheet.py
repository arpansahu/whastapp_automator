import pandas as pd
import time
import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller

keyboard = Controller()


def send_whatsapp_message(msg, mob_no):
    try:
        pywhatkit.sendwhatmsg_instantly(
            phone_no=f"+{mob_no}",
            message=msg,
            tab_close=True
        )
        time.sleep(10)
        pyautogui.click()
        time.sleep(2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print(f"Message sent! to {mob_no}")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    # Load the xlsx file

    for file in ['HOPELESS.xlsx', 'NAMELESS.xlsx', 'SHAMELESS.xlsx']:
        excel_data = pd.read_excel(file)

        for mob_no in excel_data['WhatsApp Number(with country code)']:
            print(mob_no)

            send_whatsapp_message(
                msg="JOIN MY TELEGRAM CHANNEL FOR FURTHER UPDATES"
                , mob_no= mob_no
            )






























































































































































































































