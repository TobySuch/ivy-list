<template>
  <div class="form">
    <h3>Register</h3>
    <form v-on:submit.prevent="register">
      <div class="form-group">
        <input type="email" class="form-control" id="emailInput" v-model="email" placeholder="Email">
      </div>
      <div class="form-group">
        <input type="password" class="form-control" id="passwordInput" v-model="password" placeholder="Password">
      </div>
      <div class="form-group">
        <input type="password" class="form-control" id="passwordInput2" v-model="confirm_password" placeholder="Confirm Password">
        <p v-if="this.password.length > 0 && this.confirm_password.length > 0 && this.password !== this.confirm_password" class="text-danger">Passwords must match!</p>
      </div>
      <div class="row form-group">
        <div class="col">
          <input type="text" class="form-control" v-model="first_name" placeholder="First name">
        </div>
        <div class="col">
          <input type="text" class="form-control" v-model="last_name" placeholder="Last name">
        </div>
      </div>
      <small class="form-text text-muted">These aren't required!</small>
      <button style="margin-top: 10px;" type="submit" class="btn btn-primary">Register</button>
    </form>
    <a href="/login"><button class="btn btn-link">Already have an account?</button></a>
  </div>
</template>

<script>
export default {
  name: 'RegistrationView',
  data: function () {
    return {
      email: "",
      password: "",
      confirm_password: "",
      first_name: "",
      last_name: ""
    }
  },
  methods: {
  }
}
</script>

<style scoped>
</style>
