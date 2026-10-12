const inv = require("./inventory");
inv.addItem("Widget", 10, 2.5);
inv.addItem("Gadget", 3, 10);
console.log(inv.totalValue(), inv.lowStock());
