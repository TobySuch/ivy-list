<template>
  <div>
    <h3>Here is your to do list for today:</h3>
    <div>
      <!--<ToDoItem v-for="item in current_list.todo_items" :key="item.id" :item="item"/>-->
    </div>
  </div>
</template>

<script>
export default {
  name: "ToDoView",
  data: function () {
    return {
      todo_lists: []
    }
  },
  computed: {
    most_recent_list: function() {
      if (this.todo_lists.length > 0) {
        return [...this.todo_lists].sort((a, b) => {
          return new Date(b.date) - new Date(a.date);
        })[0];
      } else {
        return null;
      }
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
        this.todo_lists = response.data;
      })
    }
  },
  mounted: function () {
    this.getToDoLists().catch((error) => {
      if (error.response.status == 401) {
        // Authentication error - Refresh access token and try again.
        this.refresh_token().then(this.getToDoLists);
      } else {
        console.error("Error contacting API");
      }
    });
  }
}
</script>

