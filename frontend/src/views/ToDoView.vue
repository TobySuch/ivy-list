<template>
  <div>
    <h3>Here is your to do list for today:</h3>
    <div v-if="todo_lists.length > 0">
      <h4>{{ todo_lists[0].date }}</h4>
      <ToDoItem v-for="item in todo_lists[0].todo_items" :key="item.id" :item="item"/>
      <h4 v-if="todo_lists[0].todo_items.length == 0">Nothing on your to do list!</h4>
    </div>
    <div v-else>
      <h4>No To Do Lists</h4>
    </div>
  </div>
</template>

<script>
import ToDoItem from '../components/ToDoItem'

export default {
  name: "ToDoView",
  components: {
    ToDoItem
  },
  data: function () {
    return {
      todo_lists: []
    }
  },
  methods: {
    getToDoLists: function() {
      return this.axios.get("/todo_list/",
      {
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + localStorage.access_token
        }
      }).then((response) => {
        this.todo_lists = [...response.data].sort((a, b) => {
          return new Date(b.date) - new Date(a.date);
        });
      });
    }
  },
  mounted: function () {
    this.getToDoLists();
  }
}
</script>

