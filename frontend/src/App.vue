<template>
  <div id="app" class="text-center container">
    <h1 id="title">Ivy List</h1>
    <LoginForm />
  </div>
</template>

<script>
//import ToDoItem from './components/ToDoItem.vue'
import LoginForm from './components/LoginForm.vue'

export default {
  name: 'App',
  components: {
//    ToDoItem,
    LoginForm
  },
  data(){
    return {
      logged_in: false,
      current_list: null
    }
  }
}
</script>

<style>
#app {
  margin-top: 60px;
}

#title {
  margin-bottom: 30px;
}

.form {
  display: inline-block;
}
</style>
