#!/usr/bin/node

exports.converter = (base) => {
  return (n) => {
    return n.toString(base);
  };
};
