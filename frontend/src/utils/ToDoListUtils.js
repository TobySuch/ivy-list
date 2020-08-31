import axios from 'axios';

export function createToDoList(date) {
  return axios.post("/todo_list/",
    JSON.stringify({
      date: date
    }),
    {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + localStorage.access_token
      }
    }).then(response => {
      return response.data;
    });
}

export function createOrGetToDoList(todo_list, date) {
  return new Promise(resolve => {
    if (todo_list == null) {
      return createToDoList(date).then(r => {
        resolve(r);
      })
    } else {
      return resolve(todo_list);
    }
  });
}