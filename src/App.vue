<template>
  <NavBar />
  <div class="mt-5 pt-5">
    <router-view />
  </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";

// import axios from "axios";

export default {
  name: "App",
  components: {
    NavBar,
  },
  computed: {
    isAuthenticated() {
      return this.$store.state.isAuthenticated;
    },
  },
  mounted() {
    this.login_check();
    console.log(this.$store.state.isAuthenticated);
  },
  methods: {
    login_check() {
      if (this.$store.state.isAuthenticated) {
        this.$router.push("/");
      } else {
        this.$router.push("/login");
      }
    },
  },
};
</script>

<style lang="css">
#app {
  background-color: #fafafa;
}
</style>
