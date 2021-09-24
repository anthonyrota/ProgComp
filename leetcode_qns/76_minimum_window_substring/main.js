/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function (s, t) {
    let required = {};
    let requiredFoundCount = 0;
    [...t].forEach((c) => {
        if (!(c in required)) {
            required[c] = 1;
            requiredFoundCount++;
        } else {
            required[c]++;
        }
    });

    let contained = {};
    let hasFoundChar = false;
    let foundCount = 0;
    let backIndex = 0;
    let bestWindow = '';

    [...s].forEach((char, idx) => {
        if (!(char in required)) {
            return;
        }

        if (!(char in contained)) {
            if (!hasFoundChar) {
                hasFoundChar = true;
                backIndex = idx;
            }
            contained[char] = 0;
        }

        contained[char]++;
        if (contained[char] === required[char]) {
            foundCount++;
            if (foundCount === requiredFoundCount) {
                let window = s.slice(backIndex, idx + 1);

                while (++backIndex < idx) {
                    const prevChar = s[backIndex - 1];
                    if (!(prevChar in required)) {
                        window = window.slice(1);
                        continue;
                    }
                    contained[prevChar]--;
                    if (contained[prevChar] < required[prevChar]) {
                        foundCount--;
                        break;
                    } else {
                        window = window.slice(1);
                    }
                }

                if (bestWindow === '' || window.length < bestWindow.length) {
                    bestWindow = window;
                }
            }
        }
    });

    return bestWindow;
};
