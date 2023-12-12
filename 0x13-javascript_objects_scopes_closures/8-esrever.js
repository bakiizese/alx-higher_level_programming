#!/usr/bin/node
exports.esrever = function (list) {
  const list2 = [];
  let j = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    list2[j++] = list[i];
  }
  return list2;
};
