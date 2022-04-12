<template>
  <!-- main feed page start -->
  <div
    class="feed wrapper container d-flex justify-content-center"
    style="background-color: #fafafa"
  >
    <div class="col-9">
      <div class="row">
        <div class="left col-8">
          <!-- stories start -->
          <FeedStory />
          <!-- stories end -->

          <!-- feed start -->
          <FeedCard v-for="feed in latestFeeds" :key="feed.id" :feed="feed" />
        </div>
        <!-- feed end -->

        <!-- side-bar start -->
        <SideBar />
        <!-- side-bar end -->
      </div>
    </div>
  </div>
  <!-- main feed page end -->
</template>

<script>
import FeedCard from "@/components/FeedCard.vue";
import SideBar from "@/components/SideBar.vue";
import FeedStory from "@/components/FeedStory.vue";

import axios from "axios";
export default {
  name: "FeedView",
  data() {
    return {
      latestFeeds: [],
    };
  },
  components: {
    FeedStory,
    SideBar,
    FeedCard,
  },
  mounted() {
    this.getFeedList();
  },
  methods: {
    getFeedList() {
      axios.defaults.headers.common["Authorization"] =
        "Token " + localStorage.getItem("token");
      axios
        .get("http://127.0.0.1:8000/api/v1/")
        .then((response) => {
          this.latestFeeds = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style lang="css">
#sidebar {
  height: 100%;
  right: 170px;
}

.story-profile-photo {
  width: 56px;
  height: 56px;
  position: relative;
}

.feed-profile-photo {
  width: 32px;
  height: 32px;
  position: relative;
}

.btn-ig {
  background-color: transparent !important;
  border: 0 !important;
  color: #007bff !important;
  font-weight: 600;
  right: 0;
  bottom: 0;
  top: 0;
  outline: none !important;
}

.btn-ig:hover,
.btn-ig:focus {
  background-color: transparent !important;
  color: #007bff !important;
}

.comment-box {
  border-top: 0.1px solid lightgray;
}

.side-profile-photo {
  width: 56px;
  height: 56px;
  position: relative;
}

.profile-info-userid {
  display: block;
  font-size: 14px;
  font-weight: 700;
}

.profile-info-name {
  font-size: 12px;
}
</style>
