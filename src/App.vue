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
};
</script>

<style lang="css">
#app {
  background-color: #fafafa;
}
</style>
