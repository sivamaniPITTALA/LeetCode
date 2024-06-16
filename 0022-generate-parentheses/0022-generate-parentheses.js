/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function (n) {
    let result = [];
    let output = [];
    backtrack(n, 0, 0, output, result);

    return result;
};

function backtrack(
    n,
    leftCount,
    rightCount,
    output,
    result
) {
    if (leftCount >= n && rightCount >= n) {
        let outputStr = output.join("");
        result.push(outputStr);
    }
    if (leftCount < n) {
        output.push("(");
        backtrack(n, leftCount + 1, rightCount, output, result);
        output.pop();
    }
    if (rightCount < leftCount) {
        output.push(")");
        backtrack(n, leftCount, rightCount + 1, output, result);
        output.pop();
    }
}