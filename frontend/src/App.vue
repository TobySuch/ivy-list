<template>
  <div id="app" class="text-center">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="/">Ivy List</a>
      <div class="navbar-nav ml-auto">
        <span class="nav-link point_cursor" @click="redirectToLogin">Log In</span>
        <span class="nav-link point_cursor" @click="redirectToRegister">Register</span>
      </div>
    </nav>
    <router-view v-on:login="login"></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function() {
    return {
      loggedIn: false
    }
  },
  methods: {
    login: function () {
      this.$router.push("/todo");
    },
    redirectToLogin: function() {
      this.$router.push("/login");
    },
    redirectToRegister: function() {
      this.$router.push("/register");
    }
  }
}
</script>

<style>
#app {
  margin: 0px;
  padding: 0px;
  /*margin-top: 60px;*/
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
