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
      let payload = {
        email: this.email,
        password: this.password
      }


      this.axios.post("http://127.0.0.1:8000/token/",
        JSON.stringify(payload),
        {
          headers: {
            'Content-Type': 'application/json'
          }
        }).then((response) => {
          localStorage.access_token = response.data.access;
          localStorage.refresh_token = response.data.refresh;
          console.log("Logged in");
      });
    }
  }
}
</script>

<style scoped>
</style>
