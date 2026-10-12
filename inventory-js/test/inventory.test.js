const test = require("node:test");
const assert = require("node:assert");
const inv = require("../inventory");

test("addItem adds an item", () => {
  inv.items.length = 0;
  inv.addItem("A", 1, 1);
  assert.strictEqual(inv.items.length, 1);
});
