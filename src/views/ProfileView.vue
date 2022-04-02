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
      axios
        .post("http://127.0.0.1:8000/auth/token/logout")

        .then(() => {
          localStorage.removeItem("token");
          axios.defaults.headers.common["Authorization"] = "";
          this.$store.commit("removeToken");
          alert("로그아웃 되었습니다.");
          this.$router.push("/");
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
