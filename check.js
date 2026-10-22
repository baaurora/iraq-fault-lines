eval(require('fs').readFileSync(__dirname + '/data.js', 'utf8') + `
const ids = new Set(EV.map(e => e[0])), ps = new Set(PEOPLE.map(p => p[0]));
console.log('motive keys w/o event:', Object.keys(MOT).filter(k => !ids.has(k)));
console.log('events w/o motives:', EV.filter(e => !MOT[e[0]]).map(e => e[0]).join(' '));
console.log('people w/o drive:', PEOPLE.filter(p => !DRIVE[p[0]]).map(p => p[0]));
console.log('missing src:', [...EV, ...PEOPLE].filter(x => !S[x[x.length === 6 ? 4 : 6]]).map(x => x[0]));
console.log(EV.length, 'events', PEOPLE.length, 'people');`);
