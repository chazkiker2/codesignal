function knapsackLight(value1, weight1, value2, weight2, maxW) {
    return Math.max(
        maxW >= weight1 && value1,
        maxW >= weight2 && value2,
        maxW >= weight1 + weight2 && value1 + value2
    )
}

function test() {
    const r1 = knapsackLight(10, 5, 6, 4, 8);
    const e1 = 10;

    console.log(r1 === e1)

    const r2 = knapsackLight(10, 5, 6, 4, 9);
    const e2 = 16;

    console.log(r2 === e2)

    const r3 = knapsackLight(5, 3, 7, 4, 6);
    const e3 = 10;

    console.log(r3 === e3)
}