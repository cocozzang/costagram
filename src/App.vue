<template>
  <NavBar />
  <div class="mt-5 pt-5">
    <router-view />
  </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";

export default {
  name: "App",
  components: {
    NavBar,
  },
  beforeMount() {
    this.islogin();
  },
  methods: {
    islogin() {
      if (!localStorage.getItem("isAuthenticated")) {
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
