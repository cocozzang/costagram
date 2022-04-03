<template>
  <div class="container d-flex justify-content-center col-9 pb-5">
    <button class="btn btn-danger btn-lg" @click="logout">Log out</button>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "ProfileView",
  methods: {
    logout() {
      axios.defaults.headers.common["Authorization"] =
        "Token " + localStorage.getItem("token");

      axios
        .post("http://127.0.0.1:8000/auth/token/logout")

        .then(() => {
          localStorage.removeItem("token");
          localStorage.removeItem("isAuthenticated");

          this.$store.commit("removeToken");

          axios.defaults.headers.common["Authorization"] = "";

          alert("로그아웃 되었습니다.");

          this.$router.push("/login");
        })

        .catch((error) => {
          alert("Something went wrong. Please try again");
          console.log(JSON.stringify(error));
        });
    },
  },
};
</script>

<style></style>
