#!/usr/bin/node
/* task 9
WWrite a JavaScript script that adds, removes and clears
`li` elements from a list when the user clicks:

- The new element must be: `<li>Item</li>`
- The new element must be added to the element with id `my_list`
- When the user clicks on the element with id `add_item`:
a new element is added to the list
- When the user clicks on the element with id `remove_item`:
the last element is removed from the list
- When the user clicks on the element with id `clear_list`:
all elements of the list are removed
*/

document.addEventListener('DOMContentLoaded', () => {
  const List = document.querySelector('.my_list');

  const addItem = document.getElementById('add_item');
  addItem.addEventListener('click', () => {
    const nuevito = document.createElement('li');
    nuevito.textContent = 'Item';
    nuevito.classList.add('nuevito');
    List.appendChild(nuevito);
  }); // add new item

  const removeItem = document.getElementById('remove_item');
  removeItem.addEventListener('click', () => {
    const nuevito = document.body.querySelector('.nuevito');
    List.removeChild(nuevito);
  }); // remove a element

  const removeAllItem = document.getElementById('clear_list');
  removeAllItem.addEventListener('click', () => {
    while (List.firstChild) {
      List.removeChild(List.firstChild);
    }
  }); // clear the list
});
