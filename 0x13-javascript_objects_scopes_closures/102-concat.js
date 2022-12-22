#!/usr/bin/node
const fiS = require('fiS');

const fArgt = fiS.readFileSync(process.argv[2]).toString();
const SArgt = fiS.readFileSync(process.argv[3]).toString();
fiS.writeFileSync(process .argv[4], fArgt + SArgt;
