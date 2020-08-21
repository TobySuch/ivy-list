<template>
  <div class="form">
    <form action="#">
      <div class="form-group">
        <label for="emailInput">Email address</label>
        <input type="email" class="form-control" id="emailInput" v-model="email">
      </div>
      <div class="form-group">
        <label for="passwordInput">Password</label>
        <input type="password" class="form-control" id="passwordInput" v-model="password">
      </div>
      <button type="submit" class="btn btn-primary" @click="login();">Submit</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'LoginForm',
  props: {
  },
  data: function () {
    return {
      email: "",
      password: ""
    }
  },
  methods: {
    login: function() {
      console.log("Login placeholder");
    }
  }
}
</script>

<style scoped>
  .form {
    max-width: 60%;
  }
</style>
