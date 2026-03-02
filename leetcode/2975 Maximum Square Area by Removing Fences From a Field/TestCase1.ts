import maximizeSquareArea from './Solution.ts';

const hFences = [
      4,   6,   7,   8,   9,  10,  11,  12,  13,  15,  16,  18,  19,  20,  21,  22, 
     24,  25,  26,  29,  30,  31,  33,  36,  37,  38,  39,  40,  41,  42,  43,  44, 
     45,  46,  49,  50,  51,  54,  57,  58,  59,  61,  62,  63,  64,  66,  68,  69, 
     70,  71,  72,  73,  74,  76,  77,  79,  80,  82,  84,  85,  86,  87,  89,  90, 
     91,  92,  94,  95,  97,  98,  99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 
    109, 111, 112, 114, 117, 120, 122, 123, 124, 125, 128, 129, 130, 131, 133, 135, 
    136, 137, 138, 139, 142, 143, 144, 146, 147, 148, 149, 150, 151, 152, 154, 156, 
    157, 158, 159, 161, 162, 163, 164, 165, 166, 168, 169, 170, 171, 172, 174, 177, 
    178, 179, 180, 183, 184, 185, 187, 188, 189, 190, 191, 192, 193, 194, 195, 197, 
    198, 200, 201, 203, 206, 207, 209, 210, 211, 212, 213, 214, 215, 216, 219, 220, 
    221, 222, 225, 226, 227, 230, 231, 234, 235, 237, 238, 239, 240, 241, 242, 243, 
    244, 245, 246, 248, 249, 250, 252, 253, 254, 255, 257, 259, 260, 261, 262, 268, 
    269, 271, 272, 273, 274, 275, 276, 277, 278, 279, 281, 283, 284, 286, 287, 289, 
    290, 292, 293, 295, 296, 297, 298, 300, 301, 304, 305, 306, 307, 308, 309, 310, 
    311, 313, 314, 316, 318, 319, 321, 322, 323, 325, 326, 327, 329, 331, 332, 333, 
    334, 335, 338, 339, 340, 341, 342, 343, 345, 346, 347, 348, 349, 350, 352, 353, 
    354, 355, 356, 357, 358, 359, 361, 368, 370, 372, 374, 375, 376, 377, 378, 379, 
    384, 385, 386, 387, 389, 390, 393, 401, 402, 403, 404, 405, 407, 408, 411, 412, 
    413, 414, 416, 418, 419, 420, 421, 423, 424, 425, 426, 427, 431, 434, 436, 437, 
    440, 442, 444, 445, 447, 451, 452, 453, 455, 458, 459, 460, 462, 463, 464, 466, 
    467, 468, 470, 471, 472, 473, 475, 477, 480, 483, 484, 489, 491, 493, 494, 495, 
    496, 499, 500, 501, 502, 503, 504, 505, 507, 508, 509, 510, 511, 512, 513, 514, 
    516, 517
];
const vFences = [
      91,  114,  137,  141,  143,  164,  174,  181,  217,  231,  279,  360,  437, 
     452,  485,  519,  528,  573,  575,  770,  785,  813,  815,  862,  908,  915, 
     959,  973,  980,  986,  995, 1090, 1124, 1135, 1205, 1318, 1329, 1403, 1450, 
    1455, 1468
];
const m = 518;
const n = 1484;

// to sort numbers in TS, you **must** supply a comparator... ANNOYING
// (a, b) => a - b to sort in ascending order...
// vFences.sort((a, b) => a - b); 

function prettyPrintArray<T>(arr: T[]) {
    console.log(`Pretty printing arr: ${arr}`)
    const maxCharsPerLine = 80;
    const maxLengthOfEl = arr.reduce<number>((acc: number, curr: T) => {
        try {
            const currAsString = String(curr)
            return currAsString.length > acc ? currAsString.length : acc
        } catch (e) {
            // TypeError ... should *never* happen, even Symbols can be converted to primitive strings
            // using String(sym), unlike most other ways to print, e.g. `${sym}` or "" + sym
            return 0
        }
    }, 0); // 0 default value for empty arrays...
    const elsPerLine = Math.floor(maxCharsPerLine / (maxLengthOfEl + 2)); // add two for comma + space
    let multiline = true;
    if (elsPerLine >= arr.length) multiline = false;
    let output: string = '[';
    for (let i = 0; i < arr.length; i++) {
        if (i % elsPerLine === 0) output += (multiline ? '\n    ' : ' ');
        // toLocaleString adds commas, handles locale-specific grouping 
        // const formattedEl: string = arr[i].toLocaleString('en-US', { useGrouping: true });
        const strEl: string = String(arr[i]); // again, should always work 
        const formattedStrEl: string = strEl.padStart(maxLengthOfEl, ' ');
        output += `${formattedStrEl}, `;
    }
    if (arr && arr.length !== 0) output = output.slice(0, -2) + (multiline ? '\n]' : ' ]');
    console.log(output);
}

// prettyPrintArray(vFences);
// prettyPrintArray(hFences);

const expected = 267289;
const result = maximizeSquareArea(m, n, hFences, vFences);
if (result !== expected) {
    console.error(`Expected ${expected}; Got ${result}`);
} else {
    console.log(`Execution succeeded`);
}