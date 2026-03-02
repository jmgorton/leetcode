function minTimeToVisitAllPoints(points: number[][]): number {
    function* pairwise<T>(iterable: Iterable<T>): IterableIterator<T[], undefined> {
    // IterableIterator<T, T> { // T[] // Generator<T[], undefined, undefined> 
        const iterator = iterable[Symbol.iterator]();
        let prev = iterator.next();
        if (prev.done) return undefined; // empty input iterable 

        let next = iterator.next();
        while (!next.done) {
            yield [prev.value, next.value];
            prev = next;
            next = iterator.next();
        }

        return undefined;
    }

    let time: number = 0;
    for (const pair of pairwise(points)) {
        const [x, y] = pair;
        time += Math.max(Math.abs(x[0] - y[0]), Math.abs(x[1] - y[1]))
    }
    return time
};