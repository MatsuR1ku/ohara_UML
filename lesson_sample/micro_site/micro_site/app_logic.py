import json
import datetime

ROBODOG_FILE = "robodog.json"


def set_my_name(name) -> None:
    """名前をJSONに保存"""
    with open(ROBODOG_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    data['my_name'] = name
    with open(ROBODOG_FILE, 'w', encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def get_my_name() -> str:
    """JSONから名前を読み出す。なければ空文字"""
    try:
        with open(ROBODOG_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data.get("my_name", "")
    except (json.JSONDecodeError, OSError):
        return ""
    
def set_new_time() -> None:
    """現在時刻をJSONに保存"""
    with open(ROBODOG_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    data['my_time'] = datetime.datetime.now().hour
    with open(ROBODOG_FILE, 'w', encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def get_my_greeting() -> str:
    """時刻に応じた挨拶を返す"""
    try:
        with open(ROBODOG_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        my_time = int(data.get("my_time", "")) or 0
        if 6 <= my_time < 12:
            return data.get("good_morning")
        elif 12 <= my_time < 18:
            return data.get("good_afternoon")
        else:
            return data.get("good_night")
    except (json.JSONDecodeError, OSError):
        return ""

def setTwoValue(first_number,second_number):
    """2つの整数をJSONに保存"""
    with open(ROBODOG_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    data['number'] = [first_number,second_number]
    with open(ROBODOG_FILE, 'w', encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def setAndGetResult() -> int:
    """JSONから2つの整数を読み出す。なければ空文字"""
    try:
        with open(ROBODOG_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            numbers = data.get("number", [0, 0])  # デフォルト値も設定
            num1 = numbers[0]
            num2 = numbers[1]
            result = num1+num2
            data["result"]=result
            return data.get("result", "")

    except (json.JSONDecodeError, OSError):
        return ""