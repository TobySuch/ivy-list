<template>
  <div>
    <h3>Here is your to do list for:</h3>
    <h4><font-awesome-icon icon="arrow-circle-left" fixed-width @click="previousDay();" class="point_cursor"/> {{ this.formatDate(current_date) }} <font-awesome-icon icon="arrow-circle-right" fixed-width @click="nextDay();" class="point_cursor"/></h4>
    <div v-if="todo_list.length > 0">
      <ToDoItem v-for="item in todo_list" :key="item.id" :item="item"/>
    </div>
    <h4 v-else>Nothing on your to do list!</h4>
    <div v-if="todo_list.length <= 6">
      <button class="btn btn-primary" style="margin-top: 10px;" @click="addToDo()">Add To Do</button>
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
      todo_list: [],
      current_date: null
    }
  },
  computed: {
  },
  methods: {
    getToDoList: function(date) {
      return this.axios.get("/todo_item/?date=" + this.formatDate(date),
      {
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + localStorage.access_token
        }
      }).then(response => {
        this.todo_list = response.data.results
      });
    },
    nextDay: function() {
      let d = new Date(this.current_date);
      d.setDate(d.getDate() + 1);
      this.current_date = d;
      this.getToDoList(this.current_date);
    },
    previousDay: function() {
      let d = new Date(this.current_date);
      d.setDate(d.getDate() - 1);
      this.current_date = d;
      this.getToDoList(this.current_date);
    }
  },
  mounted: function () {
    this.current_date = new Date();
    this.getToDoList(this.current_date);
  }
}
</script>

<style scoped>
  .point_cursor {
    cursor: pointer;
  }
</style>

