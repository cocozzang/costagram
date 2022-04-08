<template>
  <div class="container pt-5 pb-5">
    <authentication-view />
  </div>
</template>

<script>
import AuthenticationView from "./View";
export default {
  name: "LoginLayout",
  components: {
    AuthenticationView,
  },
};
</script>

<style></style>
