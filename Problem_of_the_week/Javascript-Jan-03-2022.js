/* Create a function in a language of your choice. The function should return a string with each character in the original string doubled. 
If you send the function "now" as a parameter, it should return "nnooww," and if you send "123a!", it should return "112233aa!!".
*/

function doubler(str) {
    let tempArr = [...str];
    let result = [];
    for (var i = 0; i < tempArr.length; i++) {
        result.push(tempArr[i] + tempArr[i]);
    }
    return result.join('');
}
console.log(doubler("now"));
