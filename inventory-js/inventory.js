const items = [];

function addItem(name, qty, price) {
  items.push({ name, qty, price });
}

function removeStock(name, qty) {
  const item = items.find((i) => i.name === name);
  item.qty -= qty; // crashes if item missing; can go negative
}

function totalValue() {
  return items.reduce((sum, i) => sum + i.qty * i.price, 0).toFixed(2); // returns string
}

function findByName(name) {
  return items.filter((i) => i.name.includes(name)); // case-sensitive
}

function lowStock(threshold = 5) {
  return items.filter((i) => i.qty < threshold).map((i) => i.name);
}

module.exports = { items, addItem, removeStock, totalValue, findByName, lowStock };
