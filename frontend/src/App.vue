<template>
  <div id="app" class="text-center container">
    <h1>Ivy List</h1>
    <router-view v-on:login="login"></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
  methods: {
    login: function () {
      this.$router.push("/todo")
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

.grab_cursor {
  cursor: -webkit-grab; cursor: grab;
}

.point_cursor {
  cursor: pointer;
}
</style>
