export default function maximizeSquareArea(m: number, n: number, hFences: number[], vFences: number[]): number {
    // in TS, to sort numbers you **have to** supply a comparator...
    // ANNOYING!!!
    hFences.sort((a, b) => a - b);
    vFences.sort((a, b) => a - b);

    let hLensFinal = new Set<number>();
    let hLensActive = new Set<number>();
    let ph = 1;
    for (const h of hFences.concat([m])) {
        // hLensFinal = new Set([...hLensFinal, ...hLensActive]);
        hLensActive = new Set([...hLensActive].map(hl => hl + h - ph));
        hLensActive.add(h - ph);
        hLensActive.forEach(hl => hLensFinal.add(hl));
        ph = h;
    }
    // hLensFinal = new Set([...hLensFinal, ...hLensActive]);
    // hLensActive.forEach(hl => hLensFinal.add(hl));

    let vLensFinal = new Set<number>();
    let vLensActive = new Set<number>();
    let pv = 1;
    for (const v of vFences.concat([n])) {
        // vLensFinal = new Set([...vLensFinal, ...vLensActive]);
        vLensActive = new Set([...vLensActive].map(vl => vl + v - pv));
        vLensActive.add(v - pv);
        vLensActive.forEach(vl => vLensFinal.add(vl));
        pv = v;
    }
    // vLensFinal = new Set([...vLensFinal, ...vLensActive]);
    // vLensActive.forEach(vl => vLensFinal.add(vl));

    // // const squareLens = vLensFinal.intersection(hLensFinal)
    // const squareLens = new Set([...vLensFinal].filter(vl => hLensFinal.has(vl)));

    // if (!squareLens || squareLens.size === 0) return -1;
    // const maxSquareLength = Math.max(...squareLens)

    // IMPROVEMENT from official solution:
    let maxSquareLength = 0
    vLensFinal.forEach(vl => {
        if (hLensFinal.has(vl)) maxSquareLength = Math.max(maxSquareLength, vl)
    })
    if (maxSquareLength === 0) return -1

    // // const maxSquareLength = [...squareLens].reduce((acc, curr) => Math.max(acc, curr));
    // // console.log(`${maxSquareLength}^2=${maxSquareLength**2}`);
    // // longest edge is 511, should be 517
    // // return (maxSquareLength ** 2) % (10 ** 9 + 7);
    // const maxSquareArea = maxSquareLength ** 2;
    // const mod = 10 ** 9 + 7
    // console.log(`${maxSquareLength}^2 = ${maxSquareArea}`)
    // if (maxSquareArea > mod) {
    //     console.log(`${maxSquareArea} goes into ${mod} ${Math.floor(maxSquareArea / mod)} times,
    //     and has a remainder of ${maxSquareArea % mod}`)
    // }
    // return maxSquareArea % mod;

    const maxSquareArea = BigInt(maxSquareLength) ** 2n;
    const mod = 10 ** 9 + 7
    // console.log(`${maxSquareLength}^2 = ${maxSquareArea}`)
    // if (maxSquareArea > mod) {
    //     console.log(`${maxSquareArea} goes into ${mod} ${Math.floor(maxSquareArea / mod)} times,
    //     and has a remainder of ${maxSquareArea % mod}`)
    // }
    return Number(BigInt(maxSquareArea) % BigInt(mod) as bigint);

    // and working with bigint/BigInt wrapper vs primitives in TS is also pretty annoying...
    // "Operator '%' cannot be applied to types 'BigInt' and 'bigint'."
    // "Argument of type 'BigInt' is not assignable to parameter of type 'string | number | bigint | boolean'."
};