#!/usr/bin/node
// prints if arguments are passed or if an argument is passed and if no argument informs that no argument

if (process.argv.length === 2){
console.log('No argument');
}else if (process.argv.length === 3) {
console.log('Argument found');
}else {
console.log('Arguments found');
}
