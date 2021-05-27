
const table = document.getElementById("myTable");
const addBtn = document.getElementById("add");

addBtn.addEventListener("click", addRow);

//let i = 1;

function addRow() {
  const row = table.insertRow();
  const cell1 = row.insertCell();
  const cell2 = row.insertCell();
  const cell3 = row.insertCell();
  cell1.innerHTML = "5000" ;
  cell2.innerHTML = "50%";
  cell3.innerHTML = "GGGAAAAGGGTTTACCTAATTACT";
}

const table2 = document.getElementById("table2");
const addBtn2 = document.getElementById("add1");

addBtn2.addEventListener("click", addRow1);

let x = 1;

function addRow1() {
  const row = table2.insertRow();
  const cell11 = row.insertCell();
  const cell22 = row.insertCell();
  const cell33 = row.insertCell();
  cell11.innerHTML = x++ ;
  cell22.innerHTML = "50%";
  cell33.innerHTML = "GGGAAAAGGGTTTACCTAATTACT";
}
