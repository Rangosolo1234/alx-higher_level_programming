#!/usr/bin/node
// Return number of occurences in a list

exports.nbOccurences = function (list, searchElement) {
  return (list.filter(e => e === searchElement).length);
};
