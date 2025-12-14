
function handleaddclick() {
    const numberA = document.getElementById('number_a').value;
    const numberB = document.getElementById('number_b').value;
    const A = parseInt(numberA, 10);
    const B = parseInt(numberB, 10);

    const sumresult = document.getElementById('sumresult');
    sumresult.textContent = A + B;

    const averesult = document.getElementById('averesult');
    averesult.textContent = (A + B) / 2;

    const suqresult = document.getElementById('squsumresult');
    suqresult.textContent = Math.pow(A, 2) + B ** 2;
}
