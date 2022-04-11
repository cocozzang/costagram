<template>
  <div class="right col-3 position-fixed" id="sidebar">
    <!-- side-profile start -->
    <div class="d-flex flex-row justify-content-between">
      <div class="d-flex flex-row align-items-center">
        <div
          class="rounded-circle overflow-hidden d-flex justify-content-center align-items-center border side-profile-photo me-3"
        >
          <img
            :src="this.$store.state.userInfo.profile_thumbnail"
            style="
              transform: scale(1.5);
              width: 100%;
              position: absolute;
              left: 0;
            "
          />
        </div>

        <div class="profile-info">
          <span class="profile-info-userid">{{
            this.$store.state.userInfo.nickname
          }}</span>
          <span class="profile-info-name text-muted"
            >{{ this.$store.state.userInfo.lastname
            }}{{ this.$store.state.userInfo.firstname }}</span
          >
        </div>
      </div>
      <button class="btn btn-primary btn-sm p-0 btn-ig">Switch</button>
    </div>

    <!-- side-profile end -->

    <!-- side-suggest start -->
    <div class="mt-4">
      <div class="d-flex flex-row justify-content-between">
        <small class="text-black-50 fw-bold mb-2">Suggestions For You</small>
        <small>See All</small>
      </div>

      <div>
        <div class="d-flex flex-row justify-content-between">
          <div class="d-flex flex-row align-items-center">
            <div
              class="rounded-circle overflow-hidden d-flex justify-content-conter align-items-center border feed-profile-photo me-2"
            >
              <img
                src="@/assets/cat2.jpg"
                style="
                  transform: scale(1.5);
                  width: 100%;
                  position: absolute;
                  left: 0;
                "
              />
            </div>
            <strong>Instagram</strong>
          </div>
          <button class="btn btn-primary btn-sm p-0 btn-ig">Follow</button>
        </div>
      </div>
    </div>
    <!-- side-suggest end -->
  </div>
</template>

<script>
export default {
  name: "SideBar",
};
</script>

<style></style>
