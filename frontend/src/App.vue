<template>
  <div id="app" class="text-center container">
    <ToDoItem v-for="item in current_list.todo_items" :key="item.id" :item="item"/>
  </div>
</template>

<script>
import ToDoItem from './components/ToDoItem.vue'

export default {
  name: 'App',
  components: {
    ToDoItem
  },
  data(){
    return {
      item: {
        id: 1,
        title: "Test",
        description: "This is a test item",
        created_at: "2020-08-12T13:22:57.586823Z",
        completed_at: "2020-08-12T14:01:30Z",
        priority: 1,
        todo_list: 3
      },
      current_list: {
        id: 3,
        date: "2020-08-12",
        todo_items: [
            {
                id: 1,
                title: "Test",
                description: "This is a test item",
                created_at: "2020-08-12T13:22:57.586823Z",
                completed_at: "2020-08-12T14:01:30Z",
                priority: 1,
                todo_list: 3,
                description_visible: false
            },
            {
                id: 3,
                title: "Not completed item",
                description: "This item is not completed",
                created_at: "2020-08-12T14:11:35.434502Z",
                completed_at: null,
                priority: 2,
                todo_list: 3,
                description_visible: false
            }
        ]
    }
    }
  }
}
</script>

<style>
#app {
  margin-top: 60px;
}
</style>
