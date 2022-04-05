<template>
  <NavBar />
  <PostModal />
  <div class="mt-5 pt-5">
    <router-view />
  </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import PostModal from "@/components/PostModal.vue";

export default {
  name: "App",
  components: {
    NavBar,
    PostModal,
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
