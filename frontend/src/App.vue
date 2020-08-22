<template>
  <div id="app" class="text-center container">
    <h1>Ivy List</h1>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
  data(){
    return {
      authenticated: false
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
