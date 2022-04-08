<template>
  <router-view />
</template>

<script>
export default {
  name: "App",
  components: {},
  beforeMount() {
    this.islogin();
  },
  methods: {
    islogin() {
      if (!localStorage.getItem("isAuthenticated")) {
        this.$router.push({ name: "LoginView" });
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
