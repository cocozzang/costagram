<template>
  <div
    class="feed wrapper container d-flex justify-content-center"
    style="background-color: #fafafa"
  >
    <div class="col-9">
      <form @submit.prevent="submitform">
        <div class="mb-3">
          <label for="username" class="form-label">user name</label>
          <input
            type="text"
            class="form-control"
            id="username"
            v-model="username"
          />
          <div id="emailHelp" class="form-text">
            We'll never share your email with anyone else.
          </div>
        </div>
        <div class="mb-3">
          <label for="password" class="form-label">Password</label>
          <input
            type="password"
            class="form-control"
            id="password"
            autocomplete="on"
            v-model="password"
          />
        </div>
        <button type="submit" class="btn btn-primary" @click="submitForm()">
          Log in
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "LoginView",
  data() {
    return {
      username: "",
      password: "",
      errors: [],
    };
  },
  methods: {
    submitForm() {
      axios.defaults.headers.common["Authorization"] = "";
      localStorage.removeItem("token");
      const formData = {
        username: this.username,
        password: this.password,
      };
      axios
        .post("http://127.0.0.1:8000/auth/token/login/", formData)
        .then((response) => {
          const token = response.data.auth_token;
          this.$store.commit("setToken", token);
          axios.defaults.headers.common["Authorization"] = "Token " + token;
          localStorage.setItem("token", token);
          localStorage.setItem("isAuthenticated", true);

          this.$router.push("/");
        })
        .catch((error) => {
          if (error.response) {
            for (const property in error.response.data) {
              this.errors.push(`${property}: ${error.response.data[property]}`);
              alert("로그인 실패");
            }
          } else {
            this.errors.push("Something went wrong. Please try again");
            console.log(JSON.stringify(error));
            alert("로그인 실패");
          }
        });
    },
  },
};
</script>

<style></style>
