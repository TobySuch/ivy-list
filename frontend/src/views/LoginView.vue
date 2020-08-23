<template>
  <div class="form">
    <h3>Log In</h3>
    <form v-on:submit.prevent="loginLocal">
      <div class="form-group">
        <input type="email" class="form-control" id="emailInput" v-model="email" placeholder="Email">
      </div>
      <div class="form-group">
        <input type="password" class="form-control" id="passwordInput" v-model="password" placeholder="Password">
      </div>
      <button type="submit" class="btn btn-primary">Log In</button>
    </form>
    <a href="/register"><button class="btn btn-link">Don't have an account?</button></a>
  </div>
</template>

<script>
export default {
  name: 'LoginForm',
  data: function () {
    return {
      email: "",
      password: ""
    }
  },
  methods: {
    loginLocal: function() {
      this.login(this.email, this.password);
    }
  }
}
</script>

<style scoped>
</style>
