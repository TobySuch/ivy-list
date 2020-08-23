<template>
  <div class="form">
    <h3>Register</h3>
    <form v-on:submit.prevent="register">
      <div class="form-group">
        <input type="email" class="form-control" id="emailInput" v-model="email" placeholder="Email">
        <p v-if="this.invalid_emails.includes(this.email)" class="text-danger">This email is already in use.</p>
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
      last_name: "",
      invalid_emails: []
    }
  },
  methods: {
    register: function() {
      if (this.invalid_emails.includes(this.email) ||
          this.password !== this.confirm_password) {
        return;
      }

      let payload = {
        email: this.email,
        password: this.password,
        first_name: this.first_name,
        last_name: this.last_name
      }

      this.axios.post("/users/register",
        JSON.stringify(payload),
        {
          headers: {
            'Content-Type': 'application/json'
          }
        }).then(response => {
          console.log(response.data);
        }).catch(error => {
          if (error.response.status == 400 && "email" in error.response.data) {
            if (error.response.data.email.includes("user with this email address already exists.")) {
              this.invalid_emails.push(this.email);
            }
          }
        });
    }
  }
}
</script>

<style scoped>
</style>
