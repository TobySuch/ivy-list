<template>
  <div id="app" class="text-center">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <span class="navbar-brand" @click="redirectToHome">Ivy List</span>
      <div v-if="loggedIn" class="navbar-nav ml-auto">
        <span class="navbar-text">Hello!</span>
        <span class="nav-link point_cursor" @click="logout">Log Out</span>
      </div>
      <div v-else class="navbar-nav ml-auto">
        <span class="nav-link point_cursor" @click="redirectToLogin">Log In</span>
        <span class="nav-link point_cursor" @click="redirectToRegister">Register</span>
      </div>
    </nav>
    <router-view class="container view" v-on:login="login"></router-view>
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
      this.loggedIn = true;
      this.$router.push("/todo");
    },
    redirectToLogin: function() {
      if (this.$route.name !=="Log In") {
        this.$router.push("/login");
      }
    },
    redirectToRegister: function() {
      if (this.$route.name !=="Register") {
        this.$router.push("/register");
      }
    },
    redirectToHome: function() {
      if (this.$route.name !=="Home") {
        this.$router.push("/");
      }
    },
    logout: function() {
      localStorage.removeItem("access_token");
      localStorage.removeItem("refresh_token");
      localStorage.removeItem("time_set");
      this.loggedIn = false;
      this.redirectToHome();
    }
  }
}
</script>

<style>
#app {
  margin: 0px;
  padding: 0px;
}

.view {
  margin-top: 10px;
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
