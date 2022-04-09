<template>
  <div class="container">
    <NavBar />
    <PostModal />
    <div class="mt-5 pt-5">
      <DefaultView />
    </div>
  </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
import PostModal from "@/components/PostModal.vue";
import DefaultView from "./View.vue";

export default {
  name: "DefaultLayout",
  components: {
    NavBar,
    PostModal,
    DefaultView,
  },
};
</script>

<style></style>
