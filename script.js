function validText(text) {
    console.log(text);
}

function textTolist() {
    const text = document.getElementById("text1").value;
    const splittext = text.split('');
    const resultText = document.getElementById("result");
    validText(text);
    let L = text.length;
    let newContent = ""; // まず空の文字列を準備する
    for (let i = 0; i < L; i++) { // ループの開始と終了条件も修正
        newContent += splittext[i] + "<br>"; // 要素を文字列として連結
    }
    resultText.innerHTML = newContent; // ループ終了後に一度だけHTML要素に反映
}