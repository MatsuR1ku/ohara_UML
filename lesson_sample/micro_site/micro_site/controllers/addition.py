from app_logic import setTwoValue, setAndGetResult
from utils import parse_post, render_template

def setTwoValue_controller(environ):
    method = environ["REQUEST_METHOD"]
    result_block = ""

    if method == "POST":
        data = parse_post(environ)
        first_number = int(data.get("first_number", ["0"])[0])
        second_number = int(data.get("second_number", ["0"])[0])
        setTwoValue(first_number, second_number)
        result = setAndGetResult()
        result_block = f"<p>計算結果: {result}</p>"

    return render_template(
        "boundaries/addition.html",
        result_block=result_block
    )