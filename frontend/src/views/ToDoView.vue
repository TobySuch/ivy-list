<template>
  <div>
    <h3>Here is your to do list for:</h3>
    <h4><font-awesome-icon icon="arrow-circle-left" fixed-width @click="previousDay();" class="point_cursor"/> {{ this.formatDate(current_date) }} <font-awesome-icon icon="arrow-circle-right" fixed-width @click="nextDay();" class="point_cursor"/></h4>
    <div v-if="todo_list != null">
      <ToDoItem v-for="item in todo_list.todo_items" :key="item.id" :item="item"/>
    </div>
    <h4 v-if="todo_list == null || todo_list.todo_items.length == 0">Nothing on your to do list!</h4>
    <div v-if="this.currentNumberOfItems <= 6">
      <button class="btn btn-primary" style="margin-top: 10px;" @click="addToDo()">Add To Do</button>
    </div>
  </div>
</template>

<script>
import ToDoItem from '../components/ToDoItem'
import { createOrGetToDoList } from '../utils/ToDoListUtils'

export default {
  name: "ToDoView",
  components: {
    ToDoItem
  },
  data: function () {
    return {
      todo_list: null,
      current_date: null
    }
  },
  computed: {
    currentNumberOfItems: function() {
      if (this.todo_list == null) {
        return 0;
      } else {
        return this.todo_list.todo_items.length;
      }
    }
  },
  methods: {
    getToDoList: function(date) {
      return this.axios.get("/todo_list/?date=" + this.formatDate(date),
      {
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + localStorage.access_token
        }
      }).then((response) => {
        if (response.data.results.length > 0) {
          this.todo_list = response.data.results[0];
        } else {
          this.todo_list = null;
        }
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
    },
    addToDo: function() {

      createOrGetToDoList(this.todo_list, this.formatDate(this.current_date)).then(a => {
        this.todo_list = a;
      });
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

