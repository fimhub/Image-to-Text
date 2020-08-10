'use strict';

// Init variables
let data = [];
let bars, donut, scatter = null;

d3.json('/load_data').then(d => {
    console.log(d)

    // Redefine
    data = d.users;

    // Print user count
    d3.select('#users').append('span')
        .text(data.length);

    // Instantiate
    bars = new Bars(data, 'vis1');


}).catch(err => console.log(err));